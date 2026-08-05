from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/welcome")
def get_welcome_msg():
    return {
        "message": "Welcome to FastAPI!",
    }

@app.get("/greet")
def get_greet_msg():
    return {
        "message": "Good Evening",
    }

class Course(BaseModel):
    course_id: int
    course_name: str
    course_price: float

@app.post("/course")
def add_course(course: Course):
    # logic to insert into db
    return {
        "message" : "Course Inserted"
    }