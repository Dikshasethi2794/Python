from flask import jsonify

class CustomException(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

def handle_exception(e):
    response = {
        "error": e.message if isinstance(e, CustomException) else "An unexpected error occurred"
    }
    status_code = e.status_code if isinstance(e, CustomException) else 500
    return (response), status_code