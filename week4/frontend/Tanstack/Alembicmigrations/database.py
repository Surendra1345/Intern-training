from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

Database_URL="postgresql://postgres:Surendra283@localhost:5432/student_db"
engine=create_engine(Database_URL)

Sessionlocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()



