#!/bin/bash
# Setup script for MinIO Cloud Storage Project

# Exit immediately if a command fails
set -e

echo "🔄 Updating system..."
sudo apt update

echo "📦 Installing Python venv and pip..."
sudo apt install -y python3-venv python3-pip

echo "🐍 Creating virtual environment..."
python3 -m venv venv

echo "✅ Activating virtual environment..."
source venv/bin/activate

echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

echo "🎉 Setup complete! To activate later, run: source venv/bin/activate"
