from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.logging import LoggingMiddleware
from routes.index import router
from core.config import config
from data.db import init_db

# import logging

app = FastAPI(
    title=config.app_title,
    description=config.app_description,
    version=config.app_version,
)


# logging.basicConfig(level=logging.DEBUG)
# Event handler to initialize the database on application startup
@app.on_event("startup")
def on_startup():
    """Handel application startup."""
    init_db()


# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)


@app.get("/")
def root():
    """Handel fall back route."""
    return {"message": "SkillMate Backend is running!"}


app.include_router(
    router
)  # The tags parameter is used for grouping related API endpoints in the automatically generated interactive API documentation (Swagger UI / OpenAPI UI).
# # (Optional but good for local development)
# # This block allows you to run the app directly from this file
# # by executing `python main.py`
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
