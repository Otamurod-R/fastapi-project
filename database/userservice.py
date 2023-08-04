from database.models import User
from datetime import datetime
from database import get_db

#register user
def register_user_db(name, email, user_city, phone_number, password):
    db=next(get_db())

    new_user=User(name=name, email=email, user_city=user_city, phone_number=phone_number, password=password,
                  reg_date=datetime.now())

    db.add(new_user)
    db.commit()
    return new_user.id

'''checking if the user has alredy had an account'''

def check_user_data_db(phone_number, email):
    db=next(get_db())

    '''checking database for the user'''
    checker=db.query(User).filter_by(phone_number=phone_number, email=email).first()

    '''if user has an account, we will return false'''
    if checker:
        return False
    '''if they don't have account return true'''
    return True

'''checking the user password'''
def check_user_password_email_db(email, password):
    db=next(get_db())

    '''try to find the user by email first'''
    checker=db.query(User).filter_by(email=email).first()

    '''after we find email, then we will compare password'''
    if checker:
        if checker.password==password:
            return checker.id
        else:
            return 'Wrong password '
    '''if we did not get the email'''
    return 'Wrong email has been indicated'

'''getting user personal info'''
def profile_info_db(user_id):
    db=next(get_db())

    '''finding user via their id'''
    exact_user=db.query(User).filter_by(id=user_id).first()

    '''if we have the user, we should show all the info'''
    if exact_user:
        return exact_user.email, exact_user.phone_number, \
            exact_user.user_city, exact_user.id, exact_user.name, \
            exact_user.reg_date,
    return 'No Such User account'

'''chenaging user data'''
def change_user_data(user_id, change_info, new_data):
    db=next(get_db())

    exact_user=db.query(User).filter_by(id=user_id).first()

    '''checking what personal datat user wants to change'''
    if exact_user:
        if change_info=='email':
            exact_user.email=new_data
        elif change_info=='number':
            exact_user.phone_number=new_data
        elif change_info=='name':
            exact_user.name=new_data
        elif change_info=='city':
            exact_user.user_city=new_data
        elif change_info=='password':
            exact_user.password=new_data

        db.commit()
    return 'Data has been successfully changed'

    '''if we did not find the user or he did not enter by forgetting login info'''
    return 'User was not found'

'''Resetting password'''
