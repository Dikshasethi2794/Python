from flask_restx import reqparse

# User parser
user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='Username is required and must be between 3 and 50 characters', location='json')
user_parser.add_argument('password', type=str, required=True, help='Password is required and must be at least 6 characters', location='json')
user_parser.add_argument('email', type=str, required=True, help='Valid email is required', location='json')

# Vehicle parser
#vehicle_parser = reqparse.RequestParser()
#vehicle_parser.add_argument('make', type=str, required=True, help='Make is required', location='json')
#vehicle_parser.add_argument('model', type=str, required=True, help='Model is required', location='json')
#vehicle_parser.add_argument('year', type=int, required=True, help='Year is required', location='json')
