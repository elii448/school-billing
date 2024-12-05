@echo off
echo Welcome to the School Billing Setup Wizard!

:: Check Python version
echo Checking Python version...
python --version 2>nul | findstr "3.11" >nul
if errorlevel 1 (
    echo Python 3.11 is required but not found. Please install it and try again.
    pause
    exit /b 1
)

:: Install dependencies
echo Installing dependencies...
pip install ruff==0.8.1 customtkinter==5.2.2 ctkmessagebox==2.7 ctktooltip==0.8 cx-freeze==7.2.7
if errorlevel 1 (
    echo Failed to install dependencies. Please ensure pip is available and try again.
    pause
    exit /b 1
)

:: Launch the application
echo Launching the application...
python main.py
if errorlevel 1 (
    echo Failed to launch the application. Please ensure the file "main.py" exists in this directory.
    pause
    exit /b 1
)

echo Setup complete!
pause
