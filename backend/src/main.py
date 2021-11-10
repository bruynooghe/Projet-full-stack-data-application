from typing import Optional
from fastapi import FastAPI, Header, Request, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
import json
import asyncio
import os
from starlette_exporter import PrometheusMiddleware, handle_metrics
from typing import Optional, List
import base64
import json
from sqlalchemy.orm import Session

from models import Base, engine, get_db
import schemas, models, services


app = FastAPI()


origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:3001",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
def hello_world():
    return "hello world !"

@app.post("/api/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db=db, user=user)

@app.post("/api/del_users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = services.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="This user does not exist")
    return services.delete_user(db=db, user_id=user_id)

@app.get("/api/users/", response_model=List[schemas.User])
def read_users(db: Session = Depends(get_db)):
    users = services.get_users(db)
    return users

@app.get("/api/annonces/", response_model=List[schemas.AnnonceCreate])
def read_texts(db: Session = Depends(get_db)):
    texts = services.get_texts(db)
    return texts

@app.get("/api/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = services.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/api/annonces/{annonce_id}", response_model=schemas.AnnonceCreate)
def read_annonce(annonce_id: int, db: Session = Depends(get_db)):
    db_annonce = services.get_annonce(db, annonce_id=annonce_id)
    if db_annonce is None:
        raise HTTPException(status_code=404, detail="Annonce not found")
    return db_annonce