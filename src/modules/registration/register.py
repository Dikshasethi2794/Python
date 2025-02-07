
from config.server.instance import server
from flask_restx import Resource, Namespace
from flask import request, jsonify
from modules.registration.user_model import user_model
from modules.registration.user_service import get_user_by_username, register_user
from exceptions.exception_handler import CustomException, handle_exception
from utils.parsers.common_parsers import user_parser

api = Namespace('register', description='User registration')

@api.route('/')
class Register(Resource):
        @api.expect(user_model, validate=True)
        @api.doc(description="Register a new user")
        def post(self):
            try:
                data = request.get_json()
                username = data.get('username')
                password = data.get('password')
                email = data.get('email')

                connection = request.connection
                existing_users = get_user_by_username(connection, username)

                if existing_users:
                    return existing_users, 200
                
                # Register the new user
                register_user(connection, username, password, email)
                return ({"message": "User registered successfully"}), 201
        
            except CustomException as e:
                return handle_exception(e)
            except Exception as e:
                return handle_exception(e)