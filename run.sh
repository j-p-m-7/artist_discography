#!/bin/bash

# Manually specify Python 3.11.10 to be used
PYTHON_EXEC="python3.11"

# Check the current Python version
PYTHON_VERSION=$($PYTHON_EXEC --version 2>&1)

# Extract the version number (e.g., "3.11.10")
VERSION_NUMBER=$(echo $PYTHON_VERSION | awk '{print $2}')

# If Python 3.11.10 is not installed, throw an error
if [[ $VERSION_NUMBER != "3.11.10" ]]; then
    echo "Error: Python 3.11.10 is required, but $PYTHON_VERSION is being used."
    exit 1
fi

# Install dependencies from requirements.txt
$PYTHON_EXEC -m pip install -r requirements.txt

# Run the main Python script using Python 3.11.10
$PYTHON_EXEC main.py
