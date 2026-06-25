from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import Base,get_db,engine
from models import  Student,Course
from schemas import StudentCreate,StudentResponse,CourseCreate,CourseResponse

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/student",response_model=StudentResponse)
def creat_student(student:StudentCreate,db:Session=Depends(get_db)):
    new_student=Student(name=student.name,age=student.age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/student/",response_model=list[StudentResponse])
def get_student(db:Session=Depends(get_db)):
    return db.query(Student).all()

@app.put("/student/{id}",response_model=StudentResponse)
def update_student(id:int,update:StudentCreate,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first()
    if not student:
        raise HTTPException(status_code=404,detail="Student not found")
    student.name=update.name
    student.age=update.age
    db.commit()
    db.refresh(student)
    return student

@app.delete("/student/{id}")
def delete_student(id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first()
    if not student:
        raise HTTPException(status_code=404,detail="Student not found")
    db.delete(student)
    db.commit()
    return {"Student deleted Successfully"}


@app.post("/course",response_model=CourseResponse)
def create_course(course:CourseCreate,db:Session=Depends(get_db)):
    new_course=Course(course=course.course,student_id=course.student_id)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@app.get("/course",response_model=list[CourseResponse])
def get_course(db:Session=Depends(get_db)):
    return db.query(Course).all()

@app.put("/course/{id}",response_model=CourseResponse)
def update_course(id:int,update:CourseCreate,db:Session=Depends(get_db)):
    course=db.query(Course).filter(Course.id==id).first()
    if not course:
        raise HTTPException(status_code=404,detail="Course not found")
    course.course=update.course
    course.student_id=update.student_id
    db.commit()
    db.refresh(course)
    return course

@app.delete("/course/{id}")
def delete_course(id:int,db:Session=Depends(get_db)):
    course=db.query(Course).filter(Course.id==id).first()
    if not course:
        raise HTTPException(status_code=404,detail="Course not found")
    db.delete(course)
    db.commit()
    return {"Student deleted Successfully"}