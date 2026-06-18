from fastapi import FastAPI

app=FastAPI()

@app.get("/{user}")
def root(user:str):
    return {"Name" : user,"message":"Hello world"}

@app.post("/user")
def user_created():
    return{"messege:User is created successfully"}

@app.put("/user/{id}")
def user_update(id:int):
    return{"User :{id} is successfully updated"}

@app.delete("/user/{id}")
def user_delete(id:int):
    return{"user:{id} is deleted successfully"}