from typing import Annotated, List 
from sqlmodel import Field, Session, SQLModel,  Relationship, create_engine, select

class Following(SQLModel, table=True):
    user_id: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
    following_id: int | None = Field(default=None, foreign_key="following.id", primary_key=True)