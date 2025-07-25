# ✅ Day 14 - SkillMate Backend - Docker Setup

> 💥 After 9 intense hours and 4+ hrs debugging volume issues — we finally have a working Dockerized FastAPI backend using **PostgreSQL** instead of SQLite! This README documents the working state as of **July 24**.

---

## ✅ Achievements

- [x] ✅ Dockerized FastAPI app with `uvicorn`
- [x] ✅ Switched from SQLite → PostgreSQL
- [x] ✅ Dockerized PostgreSQL container with volume persistence
- [x] ✅ Seed DB script runs only once at container startup
- [x] ✅ `.env` configuration respected inside Docker
- [x] ✅ Verified API routes accessible at `http://localhost:8000`
- [x] ✅ Removed faulty volume mount (`.backend:/app/backend`)
- [x] ✅ Full image rebuild after cache purge (`1.6GB` reclaimed)

---

## 🐘 Database: PostgreSQL via Docker

### 📦 PostgreSQL Service (docker-compose.yml)

```yaml
services:
  db:
    image: postgres:15
    container_name: skillmate-db
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: skillmate_user
      POSTGRES_PASSWORD: supersecret
      POSTGRES_DB: skillmate_db
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:

🔐 .env Example

DATABASE_URL=postgresql+psycopg2://skillmate_user:supersecret@db:5432/skillmate_db

### 🔁 SQLite → PostgreSQL Migration

    Replaced SQLite sqlite:///skillmate.db with PostgreSQL URI in .env

    Updated engine = create_engine(settings.DATABASE_URL) in db.py

    Verified DB tables auto-created via SQLModel.metadata.create_all(engine)

    Seeder script works with PostgreSQL now

### 🐳 Final Working Docker Setup
Dockerfile (root level)

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY pyproject.toml poetry.lock* requirements.txt* ./
RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY backend ./backend
COPY start.sh ./start.sh
RUN chmod +x ./start.sh

CMD ["./start.sh"]

### start.sh

#!/bin/bash
set -e

# Wait for DB to be ready
echo "⏳ Waiting for DB to be ready..."
until pg_isready -h db -U skillmate_user; do
  sleep 1
done

# Seed DB only once
if [ ! -f "/app/.seeded" ]; then
    echo "⚙️ Running database seeder..."
    PYTHONPATH=./backend/src python seeders/seed.py
    touch /app/.seeded
else
    echo "✅ DB already seeded."
fi

# Start server
PYTHONPATH=./backend/src uvicorn main:app --host 0.0.0.0 --port 8000 --reload

### ⚠️ Critical Fix

The following volume was breaking the backend:

### ❌ DO NOT DO THIS:
volumes:
  - .backend:/app/backend

This was overriding the backend folder inside the container, causing src directory not to be found.
### 🧠 Lessons Learned

    Volumes can override container contents — use with caution

    PostgreSQL + Docker needs a pg_isready check before app boot

    Seeding logic should only run once (via .seeded flag)

    Cache cleanup is sometimes necessary (docker builder prune)

### 🗂 Directory Structure (inside Docker)

/app
├── backend
│   └── src
│       ├── main.py
│       └── ...
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── start.s


