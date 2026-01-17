@echo off
title Twitch Cinema Listener
echo ========================================
echo   Twitch Cinema Listener
echo ========================================
echo.
echo Starting listener...
echo Listening for "Cinema" from Adamsteamguy
echo.
cd /d "%~dp0"
node twitch-cinema-listener.js
if errorlevel 1 (
    echo.
    echo ERROR: Failed to start!
    echo Make sure Node.js is installed and you ran: npm install
    echo.
)
pause
