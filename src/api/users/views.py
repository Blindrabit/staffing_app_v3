from flask import request
from flask_restx import Resource, Namespace, fields

from src.api.users import crud

users_namespace = Namespace("users")


user = users_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime,
        "first_name": fields.String(required=True),
        "last_name": fields.String(required=True),
        "password": fields.String(required=True),
    },
)


class User(Resource):
    @users_namespace.expect(user, validate=True)
    @users_namespace.response(201, "<user_email> was added!")
    @users_namespace.response(400, "Sorry. That email already exists.")
    def post(self):
        """Creates a new user"""
        post_data = request.get_json()
        username = post_data.get("username")
        email = post_data.get("email")
        first_name = post_data.get("first_name")
        last_name = post_data.get("last_name")
        password = post_data.get("password")

        response_object = {}
        user = crud.get_user_by_email(email=email)
        if user:
            response_object["message"] = "Sorry, that email already exists!"
            return response_object, 409
        crud.add_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        response_object["message"] = f"{username} was added!"
        return response_object, 201


users_namespace.add_resource(User, "")
