from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
app=FastAPI()

users=[
    {"name":"Surendra","age":22,"reg_no":1345},
    {"name":"Afzal","age":23,"reg_no":1953},
    {"name":"Sai","age":21,"reg_no":1292},
    {"name":"Yogi","age":20,"reg_no":1176}]

class User(BaseModel):
    name:str
    age:int
    reg_no:int


@app.get("/api/users/{age}")
def get_user(age:int):
    for user in users:
        if user.get("age")==age:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.post("/api/users/")
def create_user(user:User):
    users.append(user.dict())
    return user


@app.put("/api/users/{reg_no}")
def update_reg(reg_no:int,updated:User):
        for i,user in enumerate (users):
          if user["reg_no"]==reg_no:
            users[i]=updated.dict()
            return users[i]
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")

@app.delete("/api/users/{age}")
def delete_user(age:int):
    for i,user in enumerate(users):
        if user["age"]==age:
            users.pop(i)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detaile="User not found")