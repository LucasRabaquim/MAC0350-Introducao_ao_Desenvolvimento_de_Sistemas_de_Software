from typing import Annotated, List 
from sqlmodel import Field, Session, SQLModel,  Relationship, create_engine, select

class Follower(SQLModel, table=True):
    user_id: int | None = Field(default=None, foreign_key="user.id", primary_key=True)
    follower_id: int | None = Field(default=None, foreign_key="follower.id", primary_key=True)