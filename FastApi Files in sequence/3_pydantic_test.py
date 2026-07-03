from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

'''
zzzzzzd
class User(BaseModel):
    name:str
    age:int
    email:str
@app.post('/create_user')
def create_user(user:User):
    return{
        'message':'User Created',
        'data':user
    }
'''

class Address(BaseModel):
    city:str
    pincode:int
class User(BaseModel):
    name:str
    age:int
    address:Address
@app.post('/create_users')
def create_users(user:User):
    return user