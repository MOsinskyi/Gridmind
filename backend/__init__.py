from pydantic import BaseSettings


class AppConfig:
    host: str = "0.0.0.0"
    port: int = 8000


class Settings(BaseSettings):
    app = AppConfig()
