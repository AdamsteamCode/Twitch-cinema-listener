# How to Open the App

## Quick Start (Windows)

### Option 1: Double-click launcher (Recommended)
1. Double-click `run_app.bat` to launch the app directly

### Option 2: Install and run (First time)
1. Double-click `install_and_run.bat` to install dependencies and launch the app

### Option 3: Manual launch
Open PowerShell or Command Prompt in this folder and run:
```bash
python app.py
```
or
```bash
py app.py
```

## Troubleshooting

If you get "Python not found":
- Install Python from https://www.python.org/
- Make sure to check "Add Python to PATH" during installation

If dependencies are missing:
```bash
pip install -r requirements.txt
```

## What the App Does

The app will open a desktop window where you can:
- Configure your Twitch OAuth token
- Set your channel name (johnplayz1900)
- Start/Stop the bot
- View chat logs in real-time
- Monitor bot status
