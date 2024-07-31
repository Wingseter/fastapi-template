from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token

from database.connection import Database
from auth.hash_password import HashPassword

from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)
user_database = Database(User)
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="User does not exist"
        )
    
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)

    return {
        "message": "User created successfully"
    }

    
@user_router.post("/signin")
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user.email not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    if hash_password.vertify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token" : access_token,
            "token_type" : "Bearer"
        }
    raise HTTPException(
        status_code = status.HTTP_403_FORBIDDEN,
        detail="Wrong credentials passed"
    )
    