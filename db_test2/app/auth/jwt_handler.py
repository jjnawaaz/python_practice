from jose import jwt
import os
from datetime import datetime,timedelta
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET=os.getenv("JWT_SECRET")
ALGORITHM=os.getenv("ALGORITHM")

def create_token(data:dict):
    payload = data.copy()
    payload['exp'] = datetime.now() + timedelta(hours=24)
    return jwt.encode(payload,JWT_SECRET,algorithm=ALGORITHM)
