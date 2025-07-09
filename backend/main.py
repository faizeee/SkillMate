from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"message": "SkillMate Backend is running!"}
