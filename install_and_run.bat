@echo off
echo ========================================
echo  Twitch Cinema Listener Bot Setup
echo  For johnplayz1900
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1 || py --version >nul 2>&1 || (
    echo ERROR: Python not found!
    echo.
    echo Please install Python from https://www.python.org/
    echo.
    pause
    exit /b 1
)

echo Installing dependencies...
echo.

REM Try pip with different Python commands
python -m pip install -r requirements.txt 2>nul || py -m pip install -r requirements.txt 2>nul || python3 -m pip install -r requirements.txt 2>nul || (
    echo.
    echo ERROR: Failed to install dependencies!
    echo Please run manually: pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Dependencies installed!
echo  Starting application...
echo ========================================
echo.

REM Run the app
python app.py 2>nul || py app.py 2>nul || python3 app.py 2>nul || (
    echo.
    echo ERROR: Failed to start application!
    echo.
    pause
    exit /b 1
)

pause
