from fastapi import FastAPI
from fast_zero.schemas import UserSchema, UserPublic, UserDB, UserList

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
