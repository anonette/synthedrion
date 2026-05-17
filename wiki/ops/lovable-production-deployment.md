# Lovable Production Deployment Guide

> Created: 2026-05-13

## Overview

This guide explains how to deploy the AI Cold War simulation to production with:
- Public access via https://aicoldwar.lovable.app/
- Weekly automated 30-minute sessions
- Full session recording and replay capability
- Optional audio narration

## Architecture Options

### Option 1: Cloud Deployment (Recommended)

Deploy the FastAPI backend to a cloud service and connect Lovable to it.

**Pros:**
- Always available at public URL
- Easy automation via cloud schedulers
- Scalable and reliable

**Cons:**
- Requires cloud hosting costs
- Need to manage API keys securely

**Services to consider:**
- **Railway.app** - Simple Python app deployment with environment variables
- **Render.com** - Free tier available, good for FastAPI
- **Google Cloud Run** - Pay per use, scales to zero
- **AWS Lambda + API Gateway** - Serverless option

### Option 2: Tunnel Service

Keep backend local but expose via tunnel.

**Pros:**
- No cloud deployment needed
- Wiki stays on your machine

**Cons:**
- Computer must be on during sessions
- Less reliable for automation

**Services:**
- **ngrok** - Provides HTTPS tunnel to local port
- **Cloudflare Tunnel** - Free, more stable than ngrok
- **Tailscale Funnel** - If you use Tailscale

### Option 3: Hybrid Approach

Deploy backend to cloud but sync wiki from local.

**Pros:**
- Best of both worlds
- Wiki edits stay local
- Backend always available

**Cons:**
- More complex setup
- Need sync mechanism

## Implementation Steps

### Step 1: Prepare for Production

1. **Environment Configuration**
   ```python
   # app/config.py additions
   ALLOWED_ORIGINS = [
       "http://localhost:3000",
       "https://aicoldwar.lovable.app",
       "https://*.lovable.app"
   ]
   
   # Use environment variables for API keys
   OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
   PRODUCTION_MODE = os.getenv("PRODUCTION", "false").lower() == "true"
   ```

2. **Add Authentication**
   ```python
   # app/auth.py
   from fastapi import HTTPException, Security
   from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
   
   security = HTTPBearer()
   
   def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
       token = credentials.credentials
       if token != os.getenv("API_TOKEN", ""):
           raise HTTPException(status_code=403, detail="Invalid token")
       return token
   ```

3. **Session Persistence**
   - Move from in-memory to database (PostgreSQL/SQLite)
   - Store full session data including transcripts
   - Enable replay by session ID

### Step 2: Deploy Backend

#### For Railway.app (Recommended):

1. Create `railway.json`:
   ```json
   {
     "$schema": "https://railway.app/railway.schema.json",
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
     }
   }
   ```

2. Create `Procfile`:
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

3. Push to GitHub and connect Railway

4. Set environment variables in Railway dashboard:
   - `OPENROUTER_API_KEY`
   - `API_TOKEN` (for security)
   - `PRODUCTION=true`

### Step 3: Weekly Automation

1. **Create Scheduler Endpoint**
   ```python
   @app.post("/session/scheduled", dependencies=[Depends(verify_token)])
   async def run_scheduled_session():
       # Start session with predefined parameters
       session = await start_session({
           "prompt": get_weekly_prompt(),
           "actors": ["china", "us", "eu"],
           "mode": "debate",
           "include_shared": True
       })
       
       # Run for 30 minutes or N turns
       start_time = datetime.now()
       while (datetime.now() - start_time).seconds < 1800:  # 30 minutes
           await advance_session({"session_id": session["session_id"]})
           await asyncio.sleep(30)  # 30 seconds between turns
       
       # Generate summary
       summary = await summarize_session(session["session_id"])
       
       # Save to database for replay
       await save_session_archive(session["session_id"])
       
       return {"session_id": session["session_id"], "status": "completed"}
   ```

2. **Use Cloud Scheduler**
   - **Google Cloud Scheduler**: Create job to POST to `/session/scheduled`
   - **AWS EventBridge**: Similar scheduled Lambda trigger
   - **GitHub Actions**: Use cron schedule
   ```yaml
   # .github/workflows/weekly-session.yml
   name: Weekly AI Cold War Session
   on:
     schedule:
       - cron: '0 14 * * 1'  # Mondays at 2 PM UTC
   jobs:
     run-session:
       runs-on: ubuntu-latest
       steps:
         - name: Trigger Session
           run: |
             curl -X POST https://your-api.railway.app/session/scheduled \
               -H "Authorization: Bearer ${{ secrets.API_TOKEN }}"
   ```

### Step 4: Session Recording & Replay

1. **Enhanced Session Model**
   ```python
   class SessionArchive(BaseModel):
       session_id: str
       created_at: datetime
       completed_at: datetime
       mode: SessionMode
       actors: list[ActorName]
       prompt: str
       transcript: list[TranscriptMessage]
       summary: SessionSummary
       wiki_proposals: list[WikiProposal]
       replay_url: str  # Public replay link
       audio_url: str | None  # Optional audio narration
   ```

2. **Replay Endpoint**
   ```python
   @app.get("/replay/{session_id}")
   async def get_replay_page(session_id: str):
       return FileResponse("static/replay.html")
   
   @app.get("/api/replay/{session_id}")
   async def get_replay_data(session_id: str):
       archive = await load_session_archive(session_id)
       return {
           "session": archive,
           "events": convert_to_replay_events(archive.transcript)
       }
   ```

3. **Replay UI** (replay.html)
   - Timeline scrubber
   - Play/pause controls
   - Speed adjustment (1x, 1.5x, 2x)
   - Jump to specific turns
   - Show knowledge sources used

### Step 5: Audio Integration (Optional)

1. **Text-to-Speech Options**
   - **ElevenLabs API**: High quality, per-actor voices
   - **Google Cloud TTS**: Reliable, many languages
   - **OpenAI TTS**: Good quality, simple integration
   - **Edge TTS**: Free, runs locally

2. **Audio Generation**
   ```python
   async def generate_session_audio(session_id: str):
       archive = await load_session_archive(session_id)
       audio_segments = []
       
       for msg in archive.transcript:
           # Generate TTS for each message
           audio = await generate_tts(
               text=msg.content,
               voice=get_voice_for_actor(msg.actor)
           )
           audio_segments.append(audio)
       
       # Combine with pauses between turns
       combined = combine_audio_with_pauses(audio_segments)
       
       # Upload to storage
       audio_url = await upload_audio(combined, f"{session_id}.mp3")
       
       return audio_url
   ```

3. **Voice Configuration**
   ```python
   ACTOR_VOICES = {
       "china": {"voice_id": "mature-male-mandarin-accent", "speed": 0.95},
       "us": {"voice_id": "confident-female-american", "speed": 1.0},
       "eu": {"voice_id": "professional-male-british", "speed": 0.98},
       "human": {"voice_id": "neutral-narrator", "speed": 1.05},
       "system": {"voice_id": "alert-tone", "speed": 1.1}
   }
   ```

### Step 6: Lovable Frontend Updates

1. **Environment Configuration**
   ```javascript
   // config.js
   const API_URL = process.env.REACT_APP_API_URL || 'https://aicoldwar-api.railway.app';
   const API_TOKEN = process.env.REACT_APP_API_TOKEN;
   ```

2. **Session List Page**
   - Show all recorded sessions
   - Filter by date, actors, mode
   - Quick preview of summaries
   - Play button for replay

3. **Live Session Page**
   - Real-time updates via polling or WebSocket
   - Clean bubble UI (already implemented)
   - Download transcript/audio options

4. **Replay Player Component**
   ```jsx
   function ReplayPlayer({ sessionId }) {
     const [events, setEvents] = useState([]);
     const [currentIndex, setCurrentIndex] = useState(0);
     const [isPlaying, setIsPlaying] = useState(false);
     const [speed, setSpeed] = useState(1.0);
     
     // Load replay data
     // Implement playback logic
     // Render timeline and controls
   }
   ```

## Database Schema

```sql
-- PostgreSQL schema
CREATE TABLE sessions (
    id VARCHAR(255) PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    mode VARCHAR(50) NOT NULL,
    actors JSONB NOT NULL,
    prompt TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    transcript JSONB,
    summary JSONB,
    wiki_proposals JSONB,
    audio_url TEXT,
    replay_metadata JSONB
);

CREATE TABLE weekly_prompts (
    id SERIAL PRIMARY KEY,
    week_date DATE NOT NULL,
    prompt TEXT NOT NULL,
    theme VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_sessions_created ON sessions(created_at DESC);
CREATE INDEX idx_sessions_status ON sessions(status);
```

## Weekly Prompt Generation

```python
# app/prompts.py
import random
from datetime import datetime

PROMPT_THEMES = [
    "chip controls and supply chains",
    "AI safety and alignment",
    "compute sovereignty",
    "AI labor displacement",
    "military AI applications",
    "AI governance frameworks",
    "data localization",
    "AI standards and interoperability",
    "AGI race dynamics",
    "AI and climate change"
]

PROMPT_TEMPLATES = [
    "{actors} debate the implications of {theme} for global AI leadership.",
    "Breaking: {event}. How do {actors} respond to maintain their strategic positions?",
    "{actors} negotiate a framework for {theme} while protecting national interests.",
    "As {theme} becomes critical, {actors} must balance cooperation and competition."
]

def get_weekly_prompt():
    theme = random.choice(PROMPT_THEMES)
    template = random.choice(PROMPT_TEMPLATES)
    event = generate_plausible_event(theme)
    
    return template.format(
        actors="China, US, and EU",
        theme=theme,
        event=event
    )
```

## Security Considerations

1. **API Authentication**
   - Use bearer tokens for API access
   - Rotate tokens regularly
   - Rate limit public endpoints

2. **CORS Configuration**
   - Restrict to Lovable domains only
   - No wildcard origins in production

3. **Input Validation**
   - Sanitize all user inputs
   - Limit prompt length
   - Validate actor selections

4. **Data Privacy**
   - Don't log full API keys
   - Anonymize session data if needed
   - Clear retention policy

## Monitoring & Analytics

1. **Health Checks**
   ```python
   @app.get("/health/detailed")
   async def health_detailed():
       return {
           "status": "healthy",
           "database": check_db_connection(),
           "wiki": check_wiki_access(),
           "openrouter": check_openrouter_api(),
           "last_session": get_last_session_time(),
           "total_sessions": get_session_count()
       }
   ```

2. **Metrics to Track**
   - Sessions per week
   - Average session duration
   - Most debated topics
   - API response times
   - Error rates

3. **Alerting**
   - Failed scheduled sessions
   - API errors
   - Low credit warnings (OpenRouter)

## Cost Estimation

**Monthly costs for weekly 30-minute sessions:**
- OpenRouter API: ~$5-10 (depends on model usage)
- Railway/Render hosting: $5-20
- Database (if using managed): $7-15
- Audio generation (optional): $10-20
- **Total: $20-65/month**

## Quick Start Commands

```bash
# Deploy to Railway
railway login
railway link
railway up

# Set environment variables
railway variables set OPENROUTER_API_KEY=xxx
railway variables set API_TOKEN=xxx
railway variables set PRODUCTION=true

# Test scheduled endpoint
curl -X POST https://your-api.railway.app/session/scheduled \
  -H "Authorization: Bearer YOUR_API_TOKEN"

# Check health
curl https://your-api.railway.app/health/detailed
```

## Next Steps

1. Choose deployment option (Cloud recommended)
2. Set up database for persistence
3. Implement authentication
4. Deploy backend
5. Update Lovable frontend with API URL
6. Set up weekly scheduler
7. Test full flow
8. Add audio generation (optional)

Would you like me to implement any specific part of this plan?