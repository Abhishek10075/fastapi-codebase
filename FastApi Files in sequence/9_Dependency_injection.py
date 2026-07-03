from fastapi import FastAPI, Depends,Header, HTTPException
app=FastAPI()

'''
def common_logic():
    return{
        'message':"common logic executor"
    }
@app.get('/home')
def home(data=Depends(common_logic)):
    return data


#dependency resualbe
def get_current_user():
    return{
        'user':'Abhishek'
    }
@app.get('/profile')
def profile(user=Depends(get_current_user)):
    return user


@app.get('/dashboard')
def profile(user=Depends(get_current_user)):
    return user
'''

def varify_token(token:str=Header(None)):
    if token !='mysecrettoken':
        raise HTTPException(
            status_code=401,
            detail='Unathorized'
        )
    return{
        'user':'Authorized User'
    }

@app.get('/secure-data')
def secure_data(user=Depends(varify_token)):
    return{
        'message':'secure data acessed'
    }
