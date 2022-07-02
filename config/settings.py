from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "this$23is#%^secret"
    PROJECT_NAME: str = "FastAPI Core"
    BASE_DIR = Path(__file__).parent.parent


settings = Settings()