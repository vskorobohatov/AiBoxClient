#!/bin/bash

VENV_DIR="venv"

mkdir -p files
mkdir -p results

if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed!"
    exit 1
fi

echo "Checking virtual environment..."
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists"
else
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR

    if [ ! -d "$VENV_DIR" ]; then
        echo "Failed to create virtual environment"
        exit 1
    fi

    echo "Virtual environment created"
fi

source $VENV_DIR/bin/activate

if [ -z "$VIRTUAL_ENV" ]; then
    echo "Failed to activate virtual environment"
    exit 1
fi

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install requests