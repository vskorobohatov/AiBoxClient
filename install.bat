@echo off
set VENV_DIR=venv

echo Checking Python...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed!
    exit /b 1
)

echo Checking virtual environment...
if exist "%VENV_DIR%\Scripts\activate.bat" (
    echo Virtual environment already exists
) else (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%

    if not exist "%VENV_DIR%\Scripts\activate.bat" (
        echo Failed to create virtual environment
        exit /b 1
    )

    echo Virtual environment created
)

echo Activating virtual environment...
call "%VENV_DIR%\Scripts\activate.bat"

if not defined VIRTUAL_ENV (
    echo Failed to activate virtual environment
    exit /b 1
)

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies...
pip install requests

if not exist files (
    mkdir files
)

if not exist results (
    mkdir results
)

echo Done.
pause