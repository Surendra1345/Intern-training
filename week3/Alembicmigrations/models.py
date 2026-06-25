from sqlalchemy import Integer,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from database import Base

class Student(Base):
    __tablename__="student"

    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    name:Mapped[str]=mapped_column(String(100),nullable=True)
    age:Mapped[int]=mapped_column(Integer,nullable=True)
    courses:Mapped[list["Course"]]=relationship("Course",back_populates="student")

class Course(Base):
    __tablename__="courses"

    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    course:Mapped[str]=mapped_column(String(100),nullable=True)
    student_id:Mapped[int]=mapped_column(Integer,ForeignKey("student.id"))
    student:Mapped["Student"]=relationship("Student",back_populates="courses")

