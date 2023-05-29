from fastapi import APIRouter
from schema import Locations
import math
router=APIRouter(prefix="/distance",
    tags=["distance"])

@router.post("/")
def get_distance(values:Locations):
    x=diffrence(values.latitude_1,values.latitude_2)
    y=diffrence(values.longitude_1,values.longitude_2)  
    return({"Distance":math.sqrt((x*x)+(y*y))})

def diffrence(x,y):
    if x>y:
        return x-y
    else:
        return y-x