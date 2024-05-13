from sqlmodel import SQLModel, Field, create_engine, Session
from dailydo_todo_app import setting


def get_session():
    with Session(engine) as session:
        yield session

class User (SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str
    password: str

class Todo (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True, min_length=3, max_length=54)
    is_completed: bool = Field(default=False)
    user_id: int = Field(foreign_key="user.id")


# engine is one for whole application
connection_string: str = str(setting.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, echo=True)