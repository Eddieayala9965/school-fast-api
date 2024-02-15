from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models import Courses
from models import Students
from models import Enrollments
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhosst", 
     "http://localhosst:3000"

]
app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def home():
    return {'message': "hello world"}

@app.get('/courses')
def get_courses():
    courses = session.query(Courses)
    return courses.all()

@app.get('/students')
def get_students():
    students = session.query(Students)
    return students.all()

@app.get('/enorllments')
def get_enrollments():
    enrollments = session.query(Enrollments)
    return enrollments.all()

@app.post('/create/student')
async def create_student(id: int, name: str):
    new_student = Students(id=id, name=name)
    session.add(new_student)
    session.commit()
    return {"student added": new_student.name}

@app.post('/create/course')
async def create_course(id: int, name: str):
    new_course = Courses(id=id, name=name)
    session.add(new_course)
    session.commit()
    return {"course added": new_course.name}

@app.post('/create/enrollment')
async def create_enrollment(enrollment_id: int, student_id: int , course_id: int, enrollment_date: datetime):
    new_enrollment = Enrollments(enrollment_id=enrollment_id, student_id=student_id, course_id=course_id, enrollment_date = enrollment_date)
    session.add(new_enrollment)
    session.commit()
    return {"enrollment added": new_enrollment}

@app.delete('/student/{id}/delete')
async def remove_student(id: int):
        student = session.query(Students).filter(Students.id == id).first()
        if student is not None:
            session.query(Enrollments).filter(Enrollments.student_id == id).delete()
            session.delete(student)
            session.commit()
            return {"Deleted student": student.name}

@app.delete('/course/{id}/delete')
async def remove_course(id: int):
     course = session.query(Courses).filter(Courses.id == id).first()
     if course is not None:
          session.query(Enrollments).filter(Enrollments.course_id == id).delete()
          session.delete(course)
          session.commit()
          return {"Deleted course": course.name}

@app.put('/student/{id}/update')
async def update_student(id: int, new_name: str):
        student = session.query(Students).filter(Students.id == id).first()
        if student is not None:
            student.name = new_name
            session.commit()
            return {"Updated student": {"id": student.id, "name": student.name}}
        
@app.put('/course/{id}/update')
async def update_course(id: int, new_name: str):
        course = session.query(Courses).filter(Courses.id == id).first()
        if course is not None:
            course.name = new_name
            session.commit()
            return {"Updated student": {"id": course.id, "name": course.name}}





