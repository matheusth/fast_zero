from fastapi import FastAPI, HTTPException
from fast_zero.schemas import UserSchema, UserPublic, UserDB, UserList, Message

database = []   # fake database for simulation.

app = FastAPI()


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_db = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_db)
    return UserPublic(**user_db.model_dump())


@app.get('/users/', response_model=UserList)
def list_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    user_db = UserPublic(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_db
    return user_db


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    del database[user_id - 1]
    return {'detail': 'User deleted'}
