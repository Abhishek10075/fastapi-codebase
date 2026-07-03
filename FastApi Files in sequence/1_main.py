'''
from fastapi import FastAPI   # ← capital API

app = FastAPI()               # ← capital API

@app.get('/')
def home():
    return {'message': 'without virtual venv'}
'''


'''
First API(Hello World)
-Create basic route
-GET request
-Run Server(uvicorn)
-Swagger UI intor
-Interview questionsj

'''

from fastapi import FastAPI   

app = FastAPI()               

@app.get('/')
def home():
    return {'message': 'Welcome to fastapi'}


#About Route
@app.get('/about')
def about():
    return {'message':'This is About Page'}

#Users Route
@app.get('/users')
def users():
    return{
      'users':["Abhi","Amit"]
    }