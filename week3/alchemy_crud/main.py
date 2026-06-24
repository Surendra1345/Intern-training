from sqlalchemy import create_engine,Integer,String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
DataBase_URL="postgresql://postgres:Surendra%40283@localhost:5432/students"
engine=create_engine(DataBase_URL)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    marks:Mapped[int]=mapped_column(Integer)
    reg_no:Mapped[int]=mapped_column(Integer,unique=True)

Base.metadata.create_all(engine)

session=Session(engine)

students=[
    Student(name="Surendra",marks=92,reg_no=1345),
    Student(name="Yogi",marks=90,reg_no=1176),
    Student(name="Suri",marks=89,reg_no=1123),
    Student(name="Manvitha",marks=81,reg_no=1234),
    Student(name="Manasa",marks=86,reg_no=1243),
    Student(name="pavan",marks=87,reg_no=1453),
    Student(name="Kiran",marks=95,reg_no=1980),
    Student(name="Afzal",marks=88,reg_no=1953)
]
session.add_all(students)
session.commit()

users=session.query(Student).all()
for student in students:
    print(student.id,student.name,student.marks,student.reg_no)

student=session.query(Student).first()

student=session.query(Student,1)

student=session.query(Student).filter(Student.name=="Surendra").first()


session.query(Student).filter(Student.name=="Surendra").update({"marks":93})
session.commit()

student=session.query(Student).filter(Student.id==3).first()
session.delete(student)
session.commit()


