from typing import Annotated, List 
from sqlmodel import Field, Session, SQLModel,  Relationship, create_engine, select

class Annotation(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str 
    text: str
    book: str
    date: datetime
    # Propriedade: List[Nome Tabela] = ?
    user: List["User"] = Relationship(back_populates="annotation")