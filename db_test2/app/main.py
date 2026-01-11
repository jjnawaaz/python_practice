from fastapi import FastAPI
from app.routes.users import router as users_router
from app.middleware.auth import auth_middleware


app = FastAPI()
app.middleware('http')(auth_middleware)
app.include_router(users_router,prefix='/users',tags=['Users'])