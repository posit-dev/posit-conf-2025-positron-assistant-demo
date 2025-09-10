#!/bin/bash

# Check that brew is installed
if ! command -v brew &> /dev/null; then
    echo "Homebrew is not installed. Please install Homebrew first."
    exit 1
fi

# Install uv
echo "Installing uv..."
brew install uv

# Install Python
PYTHON_VERSION="3.13.7"
echo "Installing Python version $PYTHON_VERSION using uv..."
uv python install "$PYTHON_VERSION" --default
uv python update-shell

# Install rig
echo "Installing rig..."
brew tap r-lib/rig
brew install --cask rig

# Install R
# This is the last step because `sudo` may be required during installation and
# it may prompt for a password, which can interfere with earlier steps.
R_VERSION="4.5.1"
echo "Installing R version $R_VERSION using Rig..."
rig add "$R_VERSION"
