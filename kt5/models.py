from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ApiResponse(BaseModel):
    code: Optional[int]
    type: Optional[str]
    message: Optional[str]

class Category(BaseModel):
    id: Optional[int]
    name: Optional[str]

class Tag(BaseModel):
    id: Optional[int]
    name: Optional[str]

class Pet(BaseModel):
    id: Optional[int]
    category: Optional[Category]
    name: str
    photoUrls: List[str]
    tags: Optional[List[Tag]]
    status: Optional[str]

class Order(BaseModel):
    id: Optional[int]
    petId: Optional[int]
    quantity: Optional[int]
    shipDate: Optional[datetime]
    status: Optional[str]
    complete: Optional[bool]

class User(BaseModel):
    id: Optional[int]
    username: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    password: Optional[str]
    phone: Optional[str]
    userStatus: Optional[int]
