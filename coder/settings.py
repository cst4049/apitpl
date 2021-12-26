from pydantic import BaseSettings, Field
from typing import List


class AppSettings(BaseSettings):
    blueprints: List[str] = ['task']


app_settings = AppSettings()
