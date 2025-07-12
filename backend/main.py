from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.logging import LoggingMiddleware
from routes.skill_routes import router as skill_router

app = FastAPI()

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
    return {"message": "SkillMate Backend is running!"}
app.include_router(skill_router,prefix="/api")

# # (Optional but good for local development)
# # This block allows you to run the app directly from this file
# # by executing `python main.py`
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
