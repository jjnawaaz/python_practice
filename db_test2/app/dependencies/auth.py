from fastapi import Request,HTTPException,status

# require user login
def require_user(request: Request):
    print("in require user")
    print(request.state.user)
    if not request.state.user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is Unauthorized"
        )
    return request.state.user


# require admin login 
def require_admin(request: Request):
    print("in require admin")
    print(request.state.user)
    user = request.state.user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is Unauthorized"
        )
    if user.get('role') != 'admin':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User is unauthorized'
        )
    return user

