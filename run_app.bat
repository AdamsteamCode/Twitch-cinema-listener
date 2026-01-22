@echo off
echo ========================================
echo  Twitch Cinema Listener Bot Launcher
echo  For johnplayz1900
echo ========================================
echo.

REM Try different Python commands
python app.py 2>nul || py app.py 2>nul || python3 app.py 2>nul || (
    echo ERROR: Python not found!
    echo.
    echo Please install Python from https://www.python.org/
    echo Or ensure Python is in your PATH
    echo.
    pause
    exit /b 1
)

if errorlevel 1 (
    echo.
    echo Error running the app. Check if dependencies are installed:
    echo   pip install -r requirements.txt
    echo.
    pause
)
