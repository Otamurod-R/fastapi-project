from database.userservice import register_user_db, check_user_data_db, check_user_password_email_db,\
    change_user_data_db, profile_info_db
from fastapi import Request
from api import app
from pydantic import BaseModel
from typing import List, Dict
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False



class User(BaseModel):
    name: str
    email: str
    phone_number: int
    password: str
    user_city: str

@app.post('/api/registeration')
async def register_user(user_model:User):
    user_data=dict(user_model)
    email_checker = mail_checker(user_model.email)
    if email_checker:

        try:
            reg_user=register_user_db(**user_data)
            return {'status': 1, 'user_id': reg_user}
        except Exception as e:
            return {"status": 1, 'message': e}
    return {'status': 0, 'message': 'Invalid email'}


@app.get('/api/user')
async def get_user_info(user_id: int):
    exact_user=profile_info_db(user_id)

    return {'status':1, "message": exact_user}

@app.post('/api/login_out')
async def login_user(email: str, password: str):
    email_checker=mail_checker(email)
    if email_checker:
        login_checker=str(check_user_password_email_db(email, password))

        if login_checker.isdigit():
            return {'status': 1, 'user_id': int(login_checker)}
        return {'status': 0, 'message': login_checker}
    return {'status': 0, "message": 'Invalid email'}


@app.put('/api/change_info')
async def change_user_profile(user_id: int, change_info: str, new_data:str):
    data=change_user_data_db(user_id, change_info, new_data)

    return {'status': 1, "message": data}
