from fastapi import APIRouter,Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, SecurityScopes,OAuth2PasswordRequestForm
from events import get_db
from models import Teacher,Student,Admin
from typing import Annotated
from schema  import Token,TeacherIN
from datetime import datetime, timedelta
from authenticate import ACCESS_TOKEN_EXPIRE_MINUTES,get_current_active_user,authenticate_user,create_access_token
router=APIRouter(prefix="/school",tags=["school"])



@router.get("/hello")
def hello_end():
    return({"messsage":"Hello World"})

'''Teacher  CRUD'''
@router.get('/teacher')
def get_books(current_user: Annotated[Admin, Depends(get_current_active_user)],db: Session = Depends(get_db)):
   recs = db.query(Teacher).all()
   return recs

@router.post('/teacher')
def Teacher_Create(current_user: Annotated[Admin, Depends(get_current_active_user)],db: Session, teacher:Teacher):
    db_teacher = Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

@router.put('/teacher/update/{id}', response_model=Teacher)
def update_book(id:int,current_user: Annotated[Admin, Depends(get_current_active_user)],teacher:Teacher, db: Session = Depends(get_db)):
   teach = db.query(Teacher).filter(Teacher.id == id).first()
   teach.name=teacher.name
   db.commit()
   return db.query(Teacher).filter(Teacher.id == id).first()


@router.delete('/teacher/delete/{id}')
def del_book(id:int,current_user: Annotated[Admin, Depends(get_current_active_user)], db: Session = Depends(get_db)):
   try:
      db.query(Teacher).filter(Teacher.id == id).delete()
      db.commit()
   except Exception as e:
      raise Exception(e)
   return {"delete status": "success"}


'''Student CRUD'''
@router.get('/student')
def get_books(current_user: Annotated[Admin, Depends(get_current_active_user)],db: Session = Depends(get_db)):
   res = db.query(Student).all()
   return res

@router.post('/student')
def Student_Create(current_user: Annotated[Admin, Depends(get_current_active_user)],db: Session, student:Student,teacher_id:int):
    student= Student(**student.dict(),teacher_id=teacher_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@router.put('/student/update/{id}', response_model=Student)
def update_book(id:int,current_user: Annotated[Admin, Depends(get_current_active_user)],student:Student, db: Session = Depends(get_db)):
   stud = db.query(Student).filter(Student.id == id).first()
   stud.name=student.name
   stud.section=student.section
   stud.std=student.std
   stud.teacher_id=student.teacher_id
   db.commit()
   return db.query(Student).filter(Student.id == id).first()

@router.delete('/student/delete/{id}')
def del_book(id:int,current_user: Annotated[Admin, Depends(get_current_active_user)],db: Session = Depends(get_db)):
   try:
      db.query(Student).filter(Student.id == id).delete()
      db.commit()
   except Exception as e:
      raise Exception(e)
   return {"delete status": "success"}

@router.post('/student/add/{id}')
def Student_add_to(teach:TeacherIN,current_user: Annotated[Admin, Depends(get_current_active_user)],db: Session, student:Student,teacher_id:int):
    stud = db.query(Student).filter(Student.id == id).first()
    stud.teacher_id=teach.id
    db.commit()
    db.refresh(stud)
    return stud


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
