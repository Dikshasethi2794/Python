from fastapi import APIRouter, HTTPException, Depends
from modules.register.models import UserModel
from modules.register.service import get_user_by_username, register_user
from config.db.connection import get_db
from exceptions.exception_handler import CustomException, handle_exception

router = APIRouter()

@router.post("/register", response_model=dict, summary="Register a new user", description="Register a new user with a username, password, and email.")
def register_user_endpoint(user: UserModel, connection = Depends(get_db)):
    try:     
        print(user.username)
        existing_user = get_user_by_username(connection, user.username)
        
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")
        
        register_user(connection, user.username, user.password, user.email)
        return {"message": "User registered successfully"}
    except CustomException as e:
        return handle_exception(e)
    except Exception as e:
        return handle_exception(e)