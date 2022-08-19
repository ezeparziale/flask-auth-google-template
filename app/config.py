from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str



    class Config:
        env_file = ".env"


settings = Settings()