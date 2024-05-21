from pydantic import BaseModel, EmailStr
import uuid

class Chats(BaseModel):
    id: uuid.UUID
    type: str
    content: str



class Users(BaseModel):
    name:str
    email: EmailStr
    pasword: str
    chats: list[Chats]

