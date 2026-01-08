from fastapi import FastAPI
from db import users_collection
from bson import ObjectId
from models import User,UserUpdate,UserLogin
from auth import verify_password,hash_password
from jwt_handler import create_token
app = FastAPI()

#get user
@app.get('/users')
async def get_user():
    cursor = users_collection.find()
    list = await cursor.to_list()
    # convert the ObjectId to string here before sending response
    for item in list:
        item["_id"] = str(item["_id"])
    return {
        "Message":"Successfully fetched users",
        "Success":True,
        "Users": list
        }

#get user by id
@app.get('/users/{id}')
async def get_user_by_id(id: str):
    db_user = await users_collection.find_one({"_id":ObjectId(id)})
    # convert ObjectId format to string
    db_user["_id"]=str(db_user["_id"])
    return {
        "Message":"Successfully fetched user",
        "Success":True,
        "User":db_user
        }

# create user
@app.post('/users')
async def create_user(user: User):
    # use user.dict() to convert python object to JSON
    user = await users_collection.insert_one(user.dict())
    return {
        "Message":"User successfully created",
        "Success":True
    }

#update user
@app.patch('/users/{id}')
async def update_user(id:str, user:UserUpdate):
    updateUser = {k:v for k,v in user.dict().items() if v is not None}
    db_user = await users_collection.update_one(
        {"_id":ObjectId(id)},
        {"$set":updateUser}
    )

    if db_user.matched_count == 0:
        return {
            "Message":"User doesnt exist",
            "Success":False
        }
    else:
        return {
        "Message":"User successfully updated",
        "Success":True
    }

# delete user
@app.delete('/users/{id}')
async def delete_user(id:str):
    deletedUser = await users_collection.delete_one({"_id":ObjectId(id)})
    if deletedUser.deleted_count == 0:
        return {
            "Message":"User not found",
            "Success":False
        }
    return {
        "Message":"User deleted successfully",
        "Success":True
    }


# signup user
@app.post('/users/signup')
async def user_signup(user:User):
    existing = await users_collection.find_one({"email":user.email})
    if existing:
        return {
            "Message":"User already registered",
            "Success":False
        }
    hashed = hash_password(user.password)
    await users_collection.insert_one({
        "name":user.name,
        "email":user.email,
        "password":hashed
    })
    return {
        "Message":"User successfully signedup",
        "Success":True
    }



# login user 
@app.post('/users/login')
async def user_login(user:UserLogin):
    db_user = await users_collection.find_one({"email":user.email})
    if not db_user:
        return {
            "Message":"Invalid credentials",
            "Success":False
        }
    if not verify_password(user.password,db_user["password"]):
        return {
            "Message":"Invalid credentials",
            "Success":False
        }
    token = create_token({"_id":str(db_user["_id"])})
    return {
        "Message":"Successfully Logged In",
        "Success":True,
        "Token": token
    }