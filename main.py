import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import auth_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(auth_controller.router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)