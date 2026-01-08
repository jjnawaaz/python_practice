from fastapi import FastAPI
from db import users_collection
from bson import ObjectId
from models import User,UserUpdate
app = FastAPI()


@app.get('/')
def root_func():
    return {
        "message":"Hello World"
    }

# create user 
@app.post('/users')
async def create_user(user: User):
    db_user = await users_collection.insert_one(user.dict())
    print(db_user)
    return {
    "id": str(db_user.inserted_id),
    "message": "User created",
    "success": True
}

#get user 
@app.get('/users')
async def get_users():
    cursor = await users_collection.find()
    users = await cursor.to_list()

    # convert the ids from binary type to string
    for user in users:
        user["_id"] = str(user["_id"])
    return {
        "message":"Successfully fetched users",
        "users":users
    }

# get user by id
@app.get('/users/{id}')
async def get_user_by_id(id:str):
    user = await users_collection.find_one({"_id":ObjectId(id)})
    if user:
        # convert the mongo BinaryId into string
        user["_id"] = str(user["_id"])
        return {
            "message":"User fetched successfully",
            "user": user
        }
    else:
        return {
            "message":"No such user exists in db"
        }


# update user 
@app.patch('/users/{id}')
async def update_user(id: str, user: UserUpdate):
    # dict() converts the pydantic data to object here and items() converts the json to list of key value pairs
    # user.dict()
    # print(user.dict().items())
    update_data = {k:v for k,v in user.dict().items() if v is not None}
    print(update_data)
    db_user = await users_collection.update_one({"_id":ObjectId(id)},{"$set":update_data})
    if db_user.matched_count == 0:
       
        return {
            "message":"User doesnt exist",
            "success":False
        }
    return {
            "message":"User updated successfully",
            "success":True
        }


# delete user
@app.delete('/users/{id}')
async def delete_user(id:str):
    result = await users_collection.delete_one({"_id":ObjectId(id)})

    if result.deleted_count == 0:
        return{
            "message":"User not found to delete",
            "success":False
        }
    return {
        "message":"User deleted successfully",
        "success":True
    }

