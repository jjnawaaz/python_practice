from fastapi import Request,HTTPException,status
from jose import jwt,JWTError
import os

SECRET_KEY=os.getenv('JWT_SECRET')
ALGORITHM=os.getenv('ALGORITHM')

async def auth_middleware(request: Request,call_next):
    token = request.cookies.get('access_cookie')
    if not token:
        request.state.user = None
        return await call_next(request)
    
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        request.state.user = payload
    except JWTError:
        request.state.user = None
    return await call_next(request)
