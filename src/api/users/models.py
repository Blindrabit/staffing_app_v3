import uuid

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash

from src import db


class User(db.Model):
    # __tablename__ == "users"

    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    creation_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    first_name = db.Column(db.String(128))
    second_name = db.Column(db.String(128))
    password_hash = db.Column(db.string(128))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
