# app/models.py
from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    birth_date: str
    birth_time: str = None
    birth_place: str = None
    language: str = "en"
    use_cache: bool = True
