from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Flask
    SECRET_KEY: str

    # Postgres
    SQLALCHEMY_DATABASE_URI: str
    SQLALCHEMY_TRACK_MODIFICATIONS: str

    # Google OAuth2
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    # Google OAuth2 settings
    GOOGLE_SCOPES: list = ["openid", "email", "profile"]
    GOOGLE_REDIRECT: str = "https://127.0.0.1:5000/authorize"
    GOOGLE_AUTHORIZATION_BASE_URL: str = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_TOKEN_URL: str = "https://accounts.google.com/o/oauth2/token"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
