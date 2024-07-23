import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.settings import settings

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.run.cors_as_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.run.HOST, port=settings.run.PORT)