# from database.models import Photo, UserPost, Hashtag, Comment
from datetime import datetime
# from database import get_db
from database.models import Comment, UserPost, Hashtag, Photo
from database import get_db


### USERPOST ###
# Функция получения определенного или всех постов function(post_id)
# проверка post_id
def get_all_or_exact_post_db(post_id):
    db = next(get_db())

    # проверка
    if post_id == 0:
        return db.query(UserPost).all()

    return db.query(UserPost).filter_by(id=post_id).first()


# функция изменения текста к посту function(post_id, new_text)
def change_post_text_db(post_id, new_text):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    # проверка
    if exact_post:
        exact_post.main_text = new_text
        db.commit()

        return 'Успешно изменено'

    return 'Ошибка в данных'


# функция удаления определенного поста function(post_id)
def delete_exact_post_db(post_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    # проверка
    if exact_post:
        db.delete(exact_post)
        db.commit()

        return 'Успешно удален'

    return 'Ошибка в данных'


############


### COMMENT ###

# функция получения комментариев определенного поста function(post_id)
def get_exact_post_comments_db(post_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_post_comments = db.query(Comment).filter_by(id=post_id).first()

    # проверка
    if exact_post_comments:
        return exact_post_comments

    return []


# функция публикации комментария function(post_id, user_id, text, reg_date)
def public_comment_db(post_id, user_id, text, reg_date):
    db = next(get_db())

    new_comment = Comment(post_id=post_id, user_id=user_id,
                          text=text, reg_date=reg_date)

    db.add(new_comment)
    db.commit()

    return "Комментарий опубликован"


# функция изменения определенного комментария function(comment_id, new_comment_text)
def change_exact_comment_db(comment_id, new_comment_text):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    # проверка
    if exact_comment:
        exact_comment.text = new_comment_text
        db.commit()
        return "Успешно изменен"

    return 'Ошибка в данных'


# Удалить определенный комментарий function(comment_id)
def delete_exact_comment_db(comment_id):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    # проверка
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return "Успешно удален"

    return 'Ошибка в данных'


############

### HASHTAGS ###
# функция получения доступных в базе хештегов function(size) list[:size]
def get_some_hashtags_db(size):
    db = next(get_db())

    some_hashtags = db.query(Hashtag).all()

    return some_hashtags[:size]


# функция получения определенного хештега function(hashtag_name)
def get_exact_hashtag_db(hashtag_name):
    db = next(get_db())

    # Пробуем найти в базе такую запись
    exact_hashtag = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()

    # проверка
    if exact_hashtag:
        return exact_hashtag

    return []

### Удаление ###
# exact_user = db.query(PostPhoto).filter_by(id=post_id).first()
# db.delete(exact_user)
# db.commit()

### Изменение ###
# exact_user = db.query(PostPhoto).filter_by(id=post_id).first()
# exact_user.text = new_data
# db.commit()


#
# '''funtion to get one/all posts (post_id)'''
# def get_exact_one_post_db(post_id):
#     db=next(get_db())
#
#     '''checking'''
#     if post_id==0:
#         return db.query(UserPost).all()
#     return db.query(UserPost).filter_by(id=post_id).first()
#
#
# '''function to change user posts using post_id and new_text'''
# def change_user_post_db(post_id, new_text):
#     db=next(get_db())
#
#     exact_post=db.query(UserPost).filter_by(id=post_id).first()
#
#     if exact_post:
#
#         return exact_post.main_text==new_text
#
#     db.commit()
#
# '''function to delete post using post_id'''
# def delete_user_post_db(post_id):
#     db = next(get_db())
#
#     exact_post = db.query(UserPost).filter_by(id=post_id).first()
#
#     if exact_post:
#         return db.delete(exact_post)
#
#     db.commit()
# ################################
#
# '''function to get comments of an exact post'''
# def get_exact_one_comment_db(comment_id):
#     db=next(get_db())
#
#     '''checking'''
#     if comment_id==0:
#         return db.query(Comment).all()
#     return db.query(Comment).filter_by(id=comment_id).first()
#
# '''functoin to publish a comment using post_id, user_id, reg_date, text'''
# def make_comment_db(post_id, user_id, text):
#     db=next(get_db())
#
#     new_comment=db.Comment(post_id=post_id, user_id=user_id, text=text, reg_date=datetime.now())
#     db.add(new_comment)
#     db.commit()
#     return new_comment.id
#
# '''function to change a comment using comment_id, new_text_comment'''
# def change_user_comment_db(comment_id, new_text):
#     db = next(get_db())
#
#     exact_comment = db.query(Comment).filter_by(id=comment_id).first()
#
#     if exact_comment:
#         return exact_comment.text == new_text
#
#     db.commit()
#
# '''function to delete a comment using comment_id'''
# def delete_user_comment_db(comment_id):
#     db = next(get_db())
#
#     exact_comment = db.query(UserPost).filter_by(id=comment_id).first()
#
#     if exact_comment:
#         return db.delete(exact_comment)
#
#     db.commit()
#
#
# '''function to get some hashtags from the database using list[:size]'''
# def get_some_hashtags_db(size):
#     db=next(get_db())
#
#     exact_hashtag=db.query(Hashtag).all()
#
#     return exact_hashtag[:size]
#
#
# '''function to get exact hashtag using hashtag_name, filter_by, get'''
# def get_exact_hasgtag_db(hashtag_id):
#     db=next(get_db())
#
#     if hashtag_id==0:
#         return db.query(Hashtag).all()
#     return db.query(Hashtag).filter_by(id=hashtag_id).first()
