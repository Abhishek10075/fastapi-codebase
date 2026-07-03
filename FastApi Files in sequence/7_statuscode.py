from fastapi import FastAPI, status,HTTPException

app = FastAPI()

# Create User API
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created"
    }

# Get User API
@app.get("/get_user", status_code=status.HTTP_200_OK)
def get_user():
    return {
        "status": "Success",
        "message": "User Fetched",
        "data": {
            "name": "Abhishek",
            "age": 23
        }
    }
@app.get('/users/{user_id}')
def get_user(user_id:int):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail='User Not Found'
        )
    return {
        "id":1,
        'name':'Mohit'
    }