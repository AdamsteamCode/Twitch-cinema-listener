@echo off
echo Installing dependencies...
echo.
cd /d "%~dp0"
call npm install
if errorlevel 1 (
    echo.
    echo Installation failed!
) else (
    echo.
    echo Installation complete! You can now run START.bat
)
pause
