import os,certifi                                          # import os and certifi for os file read or read env and certificate check
from motor.motor_asyncio import AsyncIOMotorClient          
from dotenv import load_dotenv


load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")            

client = AsyncIOMotorClient(                                # equvivalent to const client = new MongoClient(uri)
    MONGO_URI,
    tls=True,                   # enable tls encryption
    tlsCAFile=certifi.where()   # send the ROOTCAFile and check the certificate here
    )
db = client.fastapi_db
users_collection = db.users
 