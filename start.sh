#!/bin/bash
set -e

# Run DB seed only once
if [ ! -f "/app/.seeded" ]; then
    echo "⚙️ Running database seeder..."
    python ./backend/src/seeders/seed.py
    touch /app/.seeded
else
    echo "Skipping seed, already done."
fi

# Start the FastAPI server
PYTHONPATH=./backend/src uvicorn main:app --host 0.0.0.0 --port 8000 --reload