from pydantic import BaseModel

class StudentCreate(BaseModel):
    name:str
    age:int

class StudentResponse(BaseModel):
    id:int
    name:str
    age:int

    class config:
        from_attribute=True

class CourseCreate(BaseModel):
    course:str
    student_id:int

class CourseResponse(BaseModel):
    id:int
    course:str
    student_id:int

    class config:
        from_attribute=True