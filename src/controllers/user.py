from flask import Blueprint
from flask_restful import Resource, Api 

app = Blueprint('user', __name__)
api = Api(app)

class User(Resource):
    def get(self, id):
        return {"id": id}

class UserLists(Resource):
    def get(self):
        return {"id": "all_user"}

api.add_resource(UserLists, '/users')
api.add_resource(User, '/users/<string:id>')
