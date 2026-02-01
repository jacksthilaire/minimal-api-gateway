# crud.py: interacts with sqlalchemy database
from sqlalchemy.orm import Session
from models import User

# CRUD operations

# Get user by ID, querying database and filtering for user_id
# Returns query object
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Get all users from the database
# Returns query object
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Creates a new user with name and email
# Returns the created user object
def create_user(db: Session, name: str, email: str):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
