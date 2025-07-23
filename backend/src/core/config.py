#-----------------------------------------------------------------
# Bellow is the the Basic way of loading dot env in the system.
#-----------------------------------------------------------------
#
#  from dotenv import load_dotenv
# import os

# load_dotenv()

# DATABASE_URL= os.getenv("DATABASE_URL","sqlite:///backend/skillmate.db")

# SECRET_KEY= os.getenv("SECRET_KEY","secretkeychangeit")
# ALGORITHM= os.getenv("ALGORITHM","HS256")
# ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv("TOKEN_EXPIRES_IN",60))
#
#------------------------------------------------------------------------
# USING pydantic : pydantic  settings is the better way to manage the env
#-----------------------------------------------------------------------

from pydantic import BaseSettings,Field

class Settings(BaseSettings):
    app_title:str = "SkillMate API"
    app_description:str = "API for SkillMate application"
    app_version:str = "0.1.0"

    db_url:str
    secret_key:str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = Field(60, env="TOKEN_EXPIRES_IN") #to manually map the Env Variable with settings variable
    
    # 👇 This is an *inner class* (also called a "Config class")
    class Config:
        env_file = ".env"

config = Settings()
        