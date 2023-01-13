from pydantic import BaseModel

class BigjpgConfig(BaseModel):
    api_token: str

class AppConfig(BaseModel):
    bigjpg: BigjpgConfig

__all__ = [ AppConfig, BigjpgConfig ]