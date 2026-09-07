from pydantic import BaseModel, Field


class LoginDTO(BaseModel):
    username: str = Field()
    password: str = Field()