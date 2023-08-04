from api import app
from fastapi import Request
from database.postservice import get_exact_post_comments_db, public_comment_db, \
    change_exact_comment_db, delete_exact_comment_db


@app.get('/api/comment')
async def get_exact_post_comments(request: Request):
    # Getting json with all the data in it
    data= await request.json()  #here will be kept all the data

    #getting key from the post_id in data
    post_id=data.get('post_id')

    if post_id:
        exact_post_comments=get_exact_post_comments_db(post_id)
        return {'status':1, 'message':exact_post_comments}
    return {'status': 0, 'message': 'wrong input from the user'}

@app.post('/api/comment')
async def public_comment(request: Request):
    data = await request.json()

    post_id=data.get('post_id')
    user_id=data.get('user_id')
    text=data.get('text')
    reg_date=data.get('reg_date')

    if post_id and user_id and text and reg_date:
        public_comment_db(post_id, user_id, text, reg_date)

        return {'status':1, 'message': 'post is published'}
    return {'status': 0, 'message': 'wrong data entry'}

@app.put('/api/comment')
async def change_exact_user_comments(request: Request):
    data = await request.json()

    comment_id=data.get('comment_id')
    new_comment=data.get('new_comment_text')

    if comment_id and new_comment:
        change_exact_comment_db(comment_id, new_comment)

        return {'status':1, 'message': 'post has been changed'}
    return {'status':0, 'message': 'wrong data entry'}


@app.delete('api/comment')
async def delete_exact_user_comment(request: Request):
    data = await request.json()

    comment_id=data.get('comment_id')

    if comment_id:
        delete_exact_comment_db(comment_id)
        return {'status': 1, 'message': 'Post has been deleted'}
    return {'status': 0, 'message': 'wong data entry'}
