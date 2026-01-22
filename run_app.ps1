# Twitch Cinema Listener Bot Launcher (PowerShell)
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Twitch Cinema Listener Bot Launcher" -ForegroundColor Cyan
Write-Host " For johnplayz1900" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Try to find Python
$python = $null
$commands = @("python", "py", "python3")

foreach ($cmd in $commands) {
    try {
        $version = & $cmd --version 2>&1
        if ($LASTEXITCODE -eq 0 -or $version -match "Python") {
            $python = $cmd
            Write-Host "Found Python: $cmd" -ForegroundColor Green
            break
        }
    } catch {
        continue
    }
}

if (-not $python) {
    Write-Host "ERROR: Python not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Python from https://www.python.org/" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Starting application..." -ForegroundColor Green
Write-Host ""

try {
    & $python app.py
} catch {
    Write-Host "Error running app: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Make sure dependencies are installed:" -ForegroundColor Yellow
    Write-Host "  pip install -r requirements.txt" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
}
