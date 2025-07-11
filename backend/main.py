from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "SkillMate Backend is running!"}

@app.get("/api/skills")
def get_skills():
    return [
        {"id": 1, "name": "JavaScript", "level": "Advanced"},
        {"id": 2, "name": "Python", "level": "Intermediate"},
        {"id": 3, "name": "FastAPI", "level": "Beginner"},
    ]

# # (Optional but good for local development)
# # This block allows you to run the app directly from this file
# # by executing `python main.py`
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
