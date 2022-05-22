from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, username: str, email: str, first_name: str, last_name: str):
        self._username = username
        self._email = email
        self._first_name = first_name
        self._last_name = last_name

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def password_hash(self):
        return self._password_hash

    def set_password_hash(self, password):
        password_hash = generate_password_hash(password=password)
        self._password_hash = password_hash

    def check_password_against_password_hash(self, password):
        return check_password_hash(self._password_hash, password)
