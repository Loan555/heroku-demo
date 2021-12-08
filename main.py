import app as app
import uvicorn
from fastapi import Depends, FastAPI
from fastapi import FastAPI, Path, Body, Depends
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
