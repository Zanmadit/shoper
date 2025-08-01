from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime, timezone
from pydantic import EmailStr
from app.customers.dao import CustomersDAO

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )

    return encoded_jwt

async def authentificate_user(email: EmailStr, password: str):
    user = await CustomersDAO.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user

