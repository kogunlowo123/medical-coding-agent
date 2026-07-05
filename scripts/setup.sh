#!/bin/bash
set -euo pipefail
echo "Setting up Medical Coding Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
