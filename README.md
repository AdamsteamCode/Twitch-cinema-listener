# Twitch Cinema Listener Bot for johnplayz1900

A desktop GUI application for managing a Twitch bot that listens to chat and handles cinema/movie-related commands for the johnplayz1900 channel.

## Features

- 🖥️ **Desktop GUI Application** - Easy-to-use interface
- 🎬 Cinema-related chat commands
- 🎥 Movie request system
- 📅 Schedule display
- 💬 Real-time chat log display
- ⚙️ Built-in configuration panel
- ▶️ Start/Stop controls

## Commands

- `!cinema` - Display cinema information
- `!movies` - List available movies
- `!request [movie name]` - Request a movie
- `!nowplaying` - Show what's currently playing
- `!schedule` - Display cinema schedule
- `!help` - Show all available commands
- `!hello` - Greet the bot

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Twitch OAuth Token:**
   - Go to https://twitchtokengenerator.com/
   - Generate a token with `chat:read` and `chat:edit` scopes
   - Or use Twitch CLI: `twitch token`

3. **Run the application:**

   **Easy way (Windows):**
   - Double-click `run_app.bat` to launch the app
   - Or double-click `install_and_run.bat` for first-time setup

   **Manual way:**
   ```bash
   python app.py
   ```
   or
   ```bash
   py app.py
   ```

4. **Configure in the app:**
   - Enter your OAuth Token in the configuration panel
   - Set your channel name (default: johnplayz1900)
   - Click "Start Bot" to begin

## Configuration

Edit the `.env` file with your credentials:

```
BOT_USERNAME=johnplayz1900
OAUTH_TOKEN=oauth:your_token_here
CHANNEL=johnplayz1900
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
```

## Notes

- The bot needs to be invited to your channel or run from an account with moderator permissions
- Keep your `.env` file secure and never commit it to version control
