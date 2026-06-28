from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.api.routes.db.database import SessionLocal
from app.api.routes.db.models import User
from app.api.routes.api.schemas import UserRegister
from app.api.routes.core.security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserRegister):

    db: Session = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return {
        "message": "User registered successfully.",
        "user_id": new_user.id
    }