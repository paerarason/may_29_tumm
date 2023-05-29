from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from sqlalchemy import Column, Integer, String,DateTime,Boolean
Base = declarative_base()

class Admin(Base):
    __tablename__="admin"
    username=Column(String(30))
    hashed_password=Column(String(150))
    email=Column(String(30))
    disabled=Column(Boolean,default=False)

class Student(Base):
    __tablename__="Student"
    id =Column(Integer, primary_key=True, index=True)
    name=Column(String(30))
    std=Column(Integer)
    section=Column(String(30))
    teacher_id=Column(String(255), ForeignKey("Teacher.id"))
    teacher=relationship("Teacher",back_populates="students")

class Teacher(Base):
    __tablename__="Teacher"
    id =Column(Integer, primary_key=True, index=True)
    name=Column(String(30))
    students=relationship("Student",uselist=False,back_populates="Student")
    
