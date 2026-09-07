import uvicorn
from fastapi import FastAPI

from controllers import auth_controller

app = FastAPI()

app.include_router(auth_controller.router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)