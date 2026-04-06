from typing import List, Optional 
from pydantic import BaseModel
from sqlmodel import Field, SQLModel,  Relationship
from datetime import datetime

# Relação User <-- 1:n --> Books
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str 
    username: str = Field(unique=True)
    password: str
    book: List["Book"] = Relationship(back_populates="user")

class Cookies(BaseModel):
    session_user: str = ""
    session_password: str = ""

# Relação Book <-- 1:n --> Anottation
class Annotation(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str 
    text: str
    public: bool 
    date: datetime = Field(default_factory=lambda: datetime.now())
    book_id: int = Field(foreign_key="book.id")
    book: Optional["Book"] = Relationship(back_populates="annotations")

# Relação User <-- 1:n --> Books
# Relação Book <-- 1:n --> Annotation
class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str 
    author: str
    summary: Optional[str]
    public: bool 
    date: datetime = Field(default_factory=lambda: datetime.now())
    user_id: int = Field(foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="book")
    annotations: List["Annotation"] = Relationship(back_populates="book")