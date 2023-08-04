from sqlalchemy import Column, DateTime, String, Integer, BigInteger, ForeignKey, Float, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__='users'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    name=Column(String, nullable=False)
    email=Column(String, nullable=False)
    user_city=Column(String, nullable=False)
    phone_number=Column(String, nullable=False)
    password=Column(String)

    reg_date=Column(DateTime)


class UserPost(Base):
    __tablename__='user_posts'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    main_text=Column(String, nullable=False)
    user_id=Column(BigInteger, ForeignKey('users.id'))

    reg_date=Column(DateTime)
    user_fk=relationship(User, lazy='subquery')


class Photo(Base):
    __tablename__='post_photos'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    post_id=Column(BigInteger, ForeignKey('user_posts.id'))
    photo_path=Column(String, nullable=False)

    post_fk=relationship(UserPost, lazy='subquery')


class Hashtag(Base):
    __tablename__='hashtags'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    hashtag_name=Column(String, nullable=False, unique=True)
    post_id=Column(BigInteger, ForeignKey('user_posts.id'))
    reg_date=Column(DateTime)

    hashtag_fk=relationship(UserPost, lazy='subquery')


class Comment(Base):
    __tablename__='comments'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    post_id=Column(BigInteger, ForeignKey('user_posts.id'))
    user_id=Column(BigInteger, ForeignKey('users.id'))
    text=Column(String, nullable=False)
    reg_date=Column(DateTime)

    user_fk=relationship(User, lazy='subquery')
    post_fk=relationship(UserPost, lazy='subquery')