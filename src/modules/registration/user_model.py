from flask_restx import fields
from config.server.instance import server

user_model = server.api.model('User', {
    'username': fields.String(required=True, description='The user username', min_length=3, max_length=50),
    'password': fields.String(required=True, description='The user password', min_length=6),
    'email': fields.String(required=True, description='The user email')
})