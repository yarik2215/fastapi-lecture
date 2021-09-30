from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}




#TODO Path parameters
# [] path parameters
# @app.get("/{item_id}")
# async def root(item_id: int):
#     return {"item": item_id}

# [] enums as parameters
# class Framework(str, Enum):
#     alexnet = "flask"
#     resnet = "fjango"
#     lenet = "fastapi"

# @app.get("/framework/{framework}")
# def framework(framework: Framework):
#     return {"framework": framework}







# TODO: Query parameters
# [] query parameters
# @app.get("/item")
# async def root(item_id: int = 0):
#     return {"item": item_id}


# [] optional parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# [] query parameter type conversion
# http://127.0.0.1:8000/items/foo?short=1
# or
# http://127.0.0.1:8000/items/foo?short=True
# or
# http://127.0.0.1:8000/items/foo?short=true
# or
# http://127.0.0.1:8000/items/foo?short=on
# or
# http://127.0.0.1:8000/items/foo?short=yes

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# when need aditional validation Query, Path, Header, Body












# TODO: Request body

from pydantic import BaseModel
from uuid import uuid4

# [] pydantic models for json parsing
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float

# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# [] more models
# class UserIn(BaseModel):
#     name: str

# class UserOut(UserIn):
#     id: str

# @app.post("/user/", response_model=UserOut, status_code=201)
# async def create_user(user: UserIn):
#     user = UserOut(**user.dict(), id=str(uuid4()))
#     return user








# TODO: Headers

from fastapi import Header

# [] headers
# @app.get("/items/")
# async def read_items(user_agent: Optional[str] = Header(None)):
#     return {"User-Agent": user_agent}










# TODO: Middlewares

import time
from fastapi import Request

# [] middlewares
# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response







# TODO: Background task

from fastapi import BackgroundTasks

# [] background tasks
# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)

# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}










# TODO: dependencies

from fastapi import Depends

# async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# [] dependencies
# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons


# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons


# [] sub dependencies 
# use_cache=False

import logging
logger = logging.getLogger("uvicorn")

# def dep_a():
#     logger.warning("A")

# def dep_b(a = Depends(dep_a)):
#     logger.warning("B")

# def dep_c(a = Depends(dep_a, use_cache=False)):
#     logger.warning("C")

# @app.get("/test")
# def test(dep_a = Depends(dep_a), dep_b = Depends(dep_b), dep_c = Depends(dep_c)):
#     return "Hello world"


# [] dependencies with yield

# async def get_db():
#     logger.warning("Open connection")
#     yield "database"
#     logger.warning("Close connection")

# async def task(database):
#     logger.warning("Some task")
#     logger.warning(f"DB: {database}")

# @app.get("/test")
# async def test(background_tasks: BackgroundTasks, database = Depends(get_db)):
#     background_tasks.add_task(task, database)
#     return database
