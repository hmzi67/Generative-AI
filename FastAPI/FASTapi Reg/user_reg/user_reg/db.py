from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine
from user_reg.settings import DATABASE_URL, TEST_DATABASE_URL

def get_session():
    with Session(engine) as session:
        yield session

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=3, max_length=22)
    email: str = Field()
    password: str = Field()

connection_string: str = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, echo=True)