# Lovable Integration Guide

## Quick Start

To connect your Lovable app at https://aicoldwar.lovable.app/ to your backend:

### 1. Deploy Backend

Choose one of these options:

#### Option A: Railway (Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and initialize
railway login
railway link

# Deploy
railway up

# Get your URL
railway open
```

#### Option B: Render
1. Connect your GitHub repo to Render
2. Set environment variables in Render dashboard
3. Deploy automatically on push

#### Option C: Local Tunnel (Testing)
```bash
# Install ngrok
choco install ngrok  # or download from ngrok.com

# Start your local server
python -m uvicorn app.main:app --reload

# In another terminal, create tunnel
ngrok http 8000

# Use the HTTPS URL provided by ngrok
```

### 2. Update Lovable Frontend

In your Lovable app, update the API configuration:

```javascript
// src/config/api.js
const API_CONFIG = {
  // Change this to your deployed URL
  baseUrl: process.env.REACT_APP_API_URL || 'https://your-app.railway.app',
  
  // Add auth header if using API token
  headers: {
    'Authorization': `Bearer ${process.env.REACT_APP_API_TOKEN}`,
    'Content-Type': 'application/json',
  }
};

// API client
export const api = {
  async startSession(prompt, actors, mode = 'debate') {
    const response = await fetch(`${API_CONFIG.baseUrl}/session/start`, {
      method: 'POST',
      headers: API_CONFIG.headers,
      body: JSON.stringify({
        prompt,
        actors,
        mode,
        include_shared: true
      })
    });
    return response.json();
  },
  
  async nextTurn(sessionId) {
    const response = await fetch(`${API_CONFIG.baseUrl}/session/message`, {
      method: 'POST',
      headers: API_CONFIG.headers,
      body: JSON.stringify({ session_id: sessionId })
    });
    return response.json();
  },
  
  async getRecentSessions() {
    const response = await fetch(`${API_CONFIG.baseUrl}/sessions/recent`, {
      headers: API_CONFIG.headers
    });
    return response.json();
  }
};
```

### 3. Environment Variables

Set these in Lovable's environment settings:

```bash
REACT_APP_API_URL=https://your-app.railway.app
REACT_APP_API_TOKEN=your-secure-token-here
```

### 4. Weekly Automation

Once deployed, set up GitHub Actions:

1. Go to your GitHub repo → Settings → Secrets
2. Add these secrets:
   - `API_URL`: Your deployed API URL
   - `API_TOKEN`: Your secure API token
3. The workflow will run automatically every Monday

Or use a cron service like cron-job.org:
- URL: `https://your-app.railway.app/session/scheduled`
- Method: POST
- Headers: `Authorization: Bearer YOUR_TOKEN`
- Schedule: Weekly

### 5. Audio Support (Optional)

To enable audio narration:

1. Install additional dependencies:
```bash
pip install edge-tts pydub
```

2. Set environment variable:
```bash
TTS_SERVICE=edge-tts  # Free option
# or
TTS_SERVICE=elevenlabs
ELEVENLABS_API_KEY=your-key
```

3. Audio will be generated automatically for completed sessions

## Example Lovable Components

### Session List Component
```jsx
import { useEffect, useState } from 'react';
import { api } from '../config/api';

export function SessionList() {
  const [sessions, setSessions] = useState([]);
  
  useEffect(() => {
    api.getRecentSessions().then(data => {
      setSessions(data.sessions);
    });
  }, []);
  
  return (
    <div className="session-list">
      <h2>Recent AI Cold War Sessions</h2>
      {sessions.map(session => (
        <div key={session.session_id} className="session-card">
          <h3>{new Date(session.created_at).toLocaleDateString()}</h3>
          <p>{session.prompt}</p>
          <div className="session-meta">
            <span>{session.mode} mode</span>
            <span>{session.turn_count} turns</span>
            {session.has_audio && <span>🔊 Audio available</span>}
          </div>
          <a href={`/replay/${session.session_id}`}>Watch Replay</a>
        </div>
      ))}
    </div>
  );
}
```

### Live Session Component
```jsx
import { useState } from 'react';
import { api } from '../config/api';

export function LiveSession() {
  const [sessionId, setSessionId] = useState(null);
  const [transcript, setTranscript] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  
  async function startSession() {
    const data = await api.startSession(
      "China, US, and EU debate AI governance",
      ["china", "us", "eu"]
    );
    setSessionId(data.session_id);
  }
  
  async function nextTurn() {
    setIsLoading(true);
    const data = await api.nextTurn(sessionId);
    if (data.messages?.[0]) {
      setTranscript(prev => [...prev, data.messages[0]]);
    }
    setIsLoading(false);
  }
  
  return (
    <div className="live-session">
      {!sessionId ? (
        <button onClick={startSession}>Start New Session</button>
      ) : (
        <>
          <div className="transcript">
            {transcript.map((msg, i) => (
              <ChatBubble key={i} message={msg} />
            ))}
          </div>
          <button onClick={nextTurn} disabled={isLoading}>
            {isLoading ? 'Thinking...' : 'Next Speaker'}
          </button>
        </>
      )}
    </div>
  );
}
```

### Chat Bubble Component
```jsx
export function ChatBubble({ message }) {
  const { actor, content, timestamp } = message;
  
  const actorStyles = {
    china: 'bubble-left bubble-red',
    us: 'bubble-right bubble-blue', 
    eu: 'bubble-left bubble-gold',
    human: 'bubble-right bubble-gray',
    system: 'bubble-center bubble-warning'
  };
  
  return (
    <div className={`chat-bubble ${actorStyles[actor] || ''}`}>
      <div className="bubble-header">
        <span className="actor-name">{actor}</span>
        <span className="timestamp">
          {new Date(timestamp).toLocaleTimeString()}
        </span>
      </div>
      <div className="bubble-content">{content}</div>
    </div>
  );
}
```

## Testing the Integration

1. **Test health endpoint**:
   ```bash
   curl https://your-api.railway.app/health
   ```

2. **Test session creation**:
   ```bash
   curl -X POST https://your-api.railway.app/session/test \
     -H "Authorization: Bearer YOUR_TOKEN"
   ```

3. **Check weekly automation**:
   - Manually trigger the GitHub Action
   - Check session was created
   - Verify replay works

## Troubleshooting

### CORS Issues
- Make sure your API URL is in the allowed origins
- Check browser console for specific CORS errors

### Authentication Fails
- Verify API_TOKEN is set correctly
- Check Authorization header format

### Session Not Persisting
- Ensure DATABASE_URL is configured
- Check database connection in health endpoint

### Audio Not Generating
- Install audio dependencies
- Check TTS service configuration
- Verify sufficient disk space

## Next Steps

1. Customize the UI in Lovable to match your design
2. Add user authentication if needed
3. Implement session sharing features
4. Add analytics tracking
5. Set up monitoring alerts

For production readiness:
- Add rate limiting
- Implement caching
- Set up CDN for static assets
- Add error tracking (Sentry)
- Configure backups