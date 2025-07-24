# Use official Python image
FROM python:3.11-slim

# Environment config
#ENV PYTHONDONTWRITEBYTECODE 1 : This sets an environment variable. When set to 1, Python won't write .pyc files (compiled bytecode files) to disk.
#ENV PYTHONUNBUFFERED 1: This also sets an environment variable. When PYTHONUNBUFFERED is set to 1, Python output (like print() statements or logs) will be sent directly to the terminal without being buffered.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Copy dependency files (pyproject, poetry lock, or requirements if exists)
COPY pyproject.toml poetry.lock* requirements.txt* ./

# Install Python deps
RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# Copy backend source code
COPY backend ./backend

# # --- ADD THESE DEBUG LINES ---
# RUN echo "--- Contents of /app/backend/src ---"
# RUN ls -la /app/backend/src

# RUN echo "--- Contents of /app/backend/src/seeders ---"
# RUN ls -la /app/backend/src/seeders
# # --- END DEBUG LINES ---

# Make startup script executable
COPY start.sh ./start.sh
RUN chmod +x ./start.sh

# Set default command
#CMD ["uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["./start.sh"]
