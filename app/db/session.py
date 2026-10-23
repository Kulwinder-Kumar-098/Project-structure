from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./tasks.db"

# engine connects SQLAlchemy to the database.
engine = create_engine(
    url= DATABASE_URL,
    connect_args= {"check_same_thread":False},
)

# SessionLocal creates database sessions.
SessionLocal = sessionmaker(
    bind= engine,
    autoflush=False,
    expire_on_commit=False
)

# get_db() provides a session to an API request and closes it afterward.
def get_db():
    db=SessionLocal()
    try :
        yield db

    finally:
        db.close()