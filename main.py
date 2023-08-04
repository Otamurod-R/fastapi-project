from fastapi import FastAPI
from database import Base, engine

'''creating a table '''
Base.metadata.create_all(bind=engine)

app=FastAPI()
from api.comments_api import comments
from api.photo_api import photos
from api.posts_api import posts
from api.hashtag_api import hastags
from api.users_api import *



# @app.get('/hello')
# async def hello():
#     return 'Hello FastApi'
#
# @app.post('/hello')
# async def post_home(name:str):
#     return {'message': f'Hello {name}'}
