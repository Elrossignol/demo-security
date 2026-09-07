from pydantic import BaseModel, EmailStr, Field


class RegisterDTO(BaseModel):
    username: str = Field()
    email: EmailStr = Field()
    role: str = Field()
    password: str = Field()