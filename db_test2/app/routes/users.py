from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.responses import JSONResponse
from bson import ObjectId
from app.db.mongodb import users_collection
from app.models.user import User,UserUpdate,UserLogin
from app.auth.hashing import verify_password,hash_password
from app.auth.jwt_handler import create_token
from app.dependencies.auth import require_user,require_admin

router = APIRouter()

# get users
@router.get('')
async def get_users():
    cursor = users_collection.find()
    list = await cursor.to_list()
    for item in list:
        item["_id"]=str(item["_id"])
    return {
        "message":"Successfully fetched users",
        "success":True,
        'list':list
    }


# get user by Id
@router.get('/{id}')
async def get_user_by_id(id:str):
    user = await users_collection.find_one({"_id":ObjectId(id)})
    if user:
        user["_id"]=str(user["_id"])
        return {
            'message':'Successfully fetched user',
            'success':True,
            'user':user
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='User not found'
    )


#delete user 
@router.delete('/{id}')
async def delete_user(id:str):
    db_user = await users_collection.delete_one({"_id":ObjectId(id)})
    if db_user.deleted_count == 0:
        return {
        'message':"Error user couldnt be deleted",
        "success":False
    }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found to delete"
    )


#update user 
@router.patch('/{id}')
async def update_user(id:str,user:UserUpdate):
    updateUser = {k:v for k,v in user.dict().items() if v is not None}
    db_user = await users_collection.update_one({'_id':ObjectId(id)},{'$set':updateUser})
    if db_user.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found to update"
        )
    else:
        return {
            'message':'user updated successfully',
            'success':True
        }
    
# make admin
@router.patch('/admin-approval/{id}')
async def make_admin(id:str,user=Depends(require_admin)):
    db_user = await users_collection.find_one({"_id":ObjectId(id)})
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    db_user["role"]="admin"
    await users_collection.update_one({"_id":ObjectId(id)},{'$set':db_user})
    return{
        "message":"User updated to admin successfully"
    }
    
#login user 
@router.post('/login')
async def user_login(user:UserLogin):
    db_user = await users_collection.find_one({"email":user.email})
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    if not verify_password(user.password,db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    token = create_token({"_id":str(db_user["_id"]),"role":db_user['role']})
    response = JSONResponse({
        "message":"Logged in successfully",
        "success":True
    })
    response.set_cookie(
        key="access_cookie",
        value=token,
        httponly=True,
        secure=True,
        samesite='strict',
        max_age=60*60*24
    )
    return response


#logout user
@router.post('/logout')
def user_logout():
    response = JSONResponse({"message":"Logged out successfully","success":True})
    response.delete_cookie("access_cookie")
    return response


#signup user
@router.post('/signup')
async def user_signup(user: User):
    # check if the user exists
    existing = await users_collection.find_one({'email':user.email})
    if existing:
        return {
            'message':'User already exists',
            'success':False
        }
    user = user.dict()
    user["role"]='user'
    user['password']=hash_password(user['password'])
    await users_collection.insert_one(user)
    if user:
        return {
            'message':'User signed Up',
            'success':True
        }
    return {
        'message':'Sign up failed',
        'success':False
    }

# user me route 
@router.post('/me')
async def my_profile(user=Depends(require_user)):
    return {"message":"Welcome user","user":user}

# admin only route
@router.post('/admin')
async def admin_profile(user=Depends(require_admin)):
    return {
        "message":"Welcome admin",
        "user":user
    }