#from events import connect_to_DB
from fastapi import FastAPI
from router import school,user,distance
def getApp():
    application=FastAPI()
    application.include_router(school.router)
    application.include_router(user.router)
    application.include_router(distance.router) 
    return application
app=getApp()

