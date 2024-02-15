from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base
from db import engine
from pydantic import BaseModel



Base = declarative_base()

class Courses(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key = True)
    name = Column(String)

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True)
    name = Column(String)

class Enrollments(Base):
    __tablename__ = 'enrollments'

    enrollment_id = Column(Integer, primary_key = True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    enrollment_date = Column(Date)

    # ForiegnKey("")*2  




Base.metadata.create_all(engine)
