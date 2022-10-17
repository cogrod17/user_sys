from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from decouple import config
from typing import Union


'''
To start a psql cli:

 psql -p 5432 fastapidb cole -h localhost
'''

DB_URL = config('DB_URL')

# "postgresql://user:password@postgresserver/db"
engine = create_engine(DB_URL, echo=True)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db() -> Union[Session, None]:
    db = Session()
    try:
        yield db
    finally:
        db.close()
