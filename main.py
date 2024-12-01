from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return{'message':'Главная страница'}

@app.get('/user/admin')
async def ad_user() :
    return{'message':'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user_id(user_id: Annotated[int, Path(ge=0, le= 100, description='Enter your id',
                                               example= 1)]) -> dict:
    return{'message':f'Вы вошли как пользователь под номером {user_id}'}

@app.get('/user/')
async def end(username: Annotated [str, Path(min_length= 5, max_length= 20, description= "Enter your name", example='UrbanUser')],
              age: Annotated[int, Path(ge = 18, le =120, description='Enter your age', example='24')]) -> dict:
    return{'message':'Информация о пользователе.','Name':username, 'Age': age}

