from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    GOOGLE_SCOPES: list = ["openid", "email", "profile"]
    GOOGLE_REDIRECT: str = "https://127.0.0.1:5000/authorize"
    GOOGLE_AUTHORIZATION_BASE_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore
