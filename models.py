# Required Libraries
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Ingredient(BaseModel):
	name: str
	quantity: str

class Recipe(BaseModel):
	title: str
	description: Optional[str] = None
	ingredient: List[Ingredient]
	instructions: str
	created_at: datetime = Field(default_factory=datetime.utcnow)

class User(BaseModel):
	username: str
	email: str
	password: str
