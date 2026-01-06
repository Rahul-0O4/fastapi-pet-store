## In this file we create the pydantic model which can be used for data validation and text validation
from pydantic import BaseModel
from typing import Optional

class PetCreate(BaseModel):
    name: str
    species: str
    age: int

class PetUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    age: Optional[int] = None
