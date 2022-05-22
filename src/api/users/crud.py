from src import db
from src.api.users.models import User


def add_user(username, email, first_name, last_name, password):
    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password=password)
    db.session.commit()
    return user


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()
