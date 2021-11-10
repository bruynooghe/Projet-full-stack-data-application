import hashlib
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import String

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session):
    return db.query(models.User).order_by(models.User.id.asc()).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hashlib.sha256(user.password.encode('utf-8')).hexdigest()
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(db: Session, user_email: String):
    user_id = get_user_by_email(db, user_email).id
    db.query(models.Annonce).filter(models.Annonce.owner_id == user_id).delete()
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()
    return 1

def get_annonce(db: Session, annonce_id: int):
    return db.query(models.Annonce).filter(models.Annonce.id == annonce_id).first()

def get_annonces(db: Session):
    return db.query(models.Annonce).all()

def get_annonces(db: Session, location: String):
    return db.query(models.Annonce).filter(models.Annonce.location == location)

def create_annonces(db: Session, annonce: schemas.AnnonceCreate, user_email: String):
    user_id = get_user_by_email(db, user_email).id
    new_annonce = models.Annonce(**annonce.dict(), owner_id=user_id)
    db.add(new_annonce)
    db.commit()
    db.refresh(new_annonce)
    return db_text