from database import get_db
from database.models import Photo

def get_all_or_exact_photo_db(photo_id, user_id):
    db=next(get_db())

    if user_id:
        exact_user_photo=db.query(Photo).filter_by(user_id=user_id).all()
        return {'status':1, 'message':exact_user_photo}
    elif photo_id:
        exact_photo=db.query(Photo).filter_by(id=photo_id).first()
        return {'status':1, 'message': exact_photo}
    else:
        all_photo=db.query(Photo).all()
        return {'status':1, 'message': all_photo}


def change_user_photo_db(photo_id, new_photo):
    db = next(get_db())
    exact_photo=db.query(Photo).filter_by(id=photo_id).first()
    if exact_photo:
        exact_photo.photo_path=new_photo
        db.commit()

        return True
    return False

def delete_photo_db(photo_id):
    db=next(get_db())

    exact_photo=db.query(Photo).filter_by(id=photo_id).first()

    if exact_photo:
        db.delete(exact_photo)
        db.commit()
        return 'photo deleted'
    return 'Photo not found'

