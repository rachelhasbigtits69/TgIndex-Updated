import os
import json
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    API_ID: int = Field(..., env="API_ID")
    API_HASH: str = Field(..., env="API_HASH")
    SESSION_STRING: str = Field(..., env="SESSION_STRING")
    SECRET_KEY: str = Field(default="a9f8e7d6c5b4a39281706f5e4d3c2b1a", env="SECRET_KEY")
    INDEX_SETTINGS: str = Field(
        default='{"index_all": true, "index_private": false, "index_group": false, "index_channel": true, "exclude_chats": [], "include_chats": []}', 
        env="INDEX_SETTINGS"
    )
    PORT: int = Field(default=7860, env="PORT")
    HOST: str = Field(default="0.0.0.0", env="HOST")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def parsed_index_settings(self) -> dict:
        try:
            return json.loads(self.INDEX_SETTINGS)
        except Exception:
            return {}

settings = Settings()
