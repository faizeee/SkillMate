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

# # --- NEW: Clean requirements.txt before installation ---
# # Remove NULL bytes from requirements.txt
# RUN sed -i 's/\x00//g' requirements.txt
# # --- END NEW ---

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

# # --- Re-add DEBUGGING for start.sh presence and permissions ---
# RUN echo "--- Debug: After COPY start.sh ---" \
#     && ls -la /app/start.sh || (echo "ERROR: start.sh not found after COPY. Aborting build." && exit 1)

# Use sed to remove Windows CR characters, then make executable
RUN sed -i 's/\r$//' ./start.sh \
    && chmod +x ./start.sh

# RUN echo "--- Debug: After sed and chmod +x ---" \
#     && ls -la /app/start.sh || (echo "ERROR: start.sh not found or permissions incorrect after processing. Aborting build." && exit 1)
# # --- END DEBUGGING for start.sh ---


# Set default command
#CMD ["uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["./start.sh"]
