from jose import jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv()

secret = os.getenv("JWT_SECRET")
algorithm = os.getenv("ALGORITHM")

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(payload, secret, algorithm=algorithm)