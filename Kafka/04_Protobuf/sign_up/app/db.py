from sqlmodel import Session, SQLModel, Field, create_engine
from app import settings

def get_session():
    with Session(engine) as session:
        yield session

class User (SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str
    password: str


# engine is one for whole application
connection_string: str = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, echo=True)