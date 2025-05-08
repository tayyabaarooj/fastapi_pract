from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

class Data(BaseModel):
    name : str

@app.post ("/create/")   
async def create(data:Data,):
    return{"data":data}
app= FastAPI()
@app.get("/test/{item_id}/")
async def test(item_id:str, query= int =1):
    return {"hello":item_id}
    
