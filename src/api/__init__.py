from flask_restx import Api

from src.api.users.views import users_namespace

api = Api(version="1.0", title="Users API", doc="/doc")

api.add_namespace(users_namespace, path="/users")
