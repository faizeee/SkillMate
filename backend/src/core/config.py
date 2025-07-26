# -----------------------------------------------------------------
# Bellow is the the Basic way of loading dot env in the system.
# -----------------------------------------------------------------
#
#  from dotenv import load_dotenv
# import os

# load_dotenv()

# DATABASE_URL= os.getenv("DATABASE_URL","sqlite:///backend/skillmate.db")

# SECRET_KEY= os.getenv("SECRET_KEY","secretkeychangeit")
# ALGORITHM= os.getenv("ALGORITHM","HS256")
# ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv("TOKEN_EXPIRES_IN",60))
#
# ------------------------------------------------------------------------
# USING pydantic : pydantic  settings is the better way to manage the env
# -----------------------------------------------------------------------

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """This class represents a configuration settings from system."""

    app_title: str = "SkillMate API"
    app_description: str = "API for SkillMate application"
    app_version: str = "0.1.0"

    # --- THE CRITICAL CHANGE FOR REQUIRED FIELDS ---
    # For required fields, Pydantic-settings expects the environment variable
    # to match the snake_case field name converted to UPPER_CASE by default.
    # So, 'db_url' expects 'DB_URL', and 'secret_key' expects 'SECRET_KEY'.
    # DO NOT use env="..." for these if you want to rely on the default mapping
    # and they are truly required with no default value.
    # These are required and will look for DATABASE_URL and SECRET_KEY env vars
    database_url: str = "sqlite:///backend/skillmate.db"
    secret_key: str

    algorithm: str = "HS256"
    access_token_expire_minutes: int = Field(
        30, env="TOKEN_EXPIRES_IN"
    )  # to manually map the Env Variable with settings variable

    model_config = SettingsConfigDict(env_file="backend/.env", extra="ignore")


config = Settings()

# try:
#     print("\n--- Settings Loaded Successfully! ---")
#     print(f"App Title: {config.app_title}")
#     print(f"DB URL: {config.database_url}")
#     print(f"Secret Key: {config.secret_key}")
#     print(f"Access Token Expire Minutes: {config.access_token_expire_minutes}")

# except Exception as e:
#     print(f"\n--- ERROR DURING SETTINGS LOAD ---")
#     print(f"Error type: {type(e).__name__}")
#     print(f"Error message: {e}")
