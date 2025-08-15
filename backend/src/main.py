from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from middlewares.logging import LoggingMiddleware
from routes.index import router
from core.config import config
from data.db import init_db

# import logging


# Event handler to initialize the database on application startup
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Handel application startup."""
    init_db()
    yield


app = FastAPI(
    title=config.app_title,
    description=config.app_description,
    version=config.app_version,
    lifespan=lifespan,
)


@app.middleware("http")
async def preflight_middleware(request: Request, call_next):
    """Handel OPTIONS request."""
    # Intercept all OPTIONS requests before they hit route dependencies
    if request.method == "OPTIONS":
        # Empty JSON body with 200 OK
        return JSONResponse(content={}, status_code=200)
    # Continue normally for other requests
    return await call_next(request)


# logging.basicConfig(level=logging.DEBUG)

# @app.on_event("startup")
# async def on_startup():
#     """Handel application startup."""
#     await init_redis()
#     init_db()


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
