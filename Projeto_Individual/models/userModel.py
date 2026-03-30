from typing import Annotated, List 
from sqlmodel import Field, Session, SQLModel,  Relationship, create_engine, select

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str 
    email: str
    password: str
    date_birth: str | None
    # Propriedade: List[Nome Tabela] = ?
    annotations: List["Annotation"] = Relationship(back_populates="user")