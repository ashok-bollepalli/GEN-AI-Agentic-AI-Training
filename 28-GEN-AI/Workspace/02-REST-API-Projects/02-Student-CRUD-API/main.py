from fastapi import FastAPI
from pydantic import BaseModel

import db

app = FastAPI()

# Runs once when the application starts
@app.on_event("startup")
def startup():
    db.create_table()

class Student(BaseModel):
    name: str
    course: str
    fee : float

@app.post("/student", status_code=201)
def create_student(student: Student):
    return db.create_student(student)

@app.get("/students")
def get_all_students():
    return db.get_students()

@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    return db.get_student_by_id(student_id)