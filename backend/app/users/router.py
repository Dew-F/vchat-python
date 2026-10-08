from fastapi import APIRouter, Depends, status

from app.auth.deps import get_current_user
from app.core.db.session import SessionDep
from app.users.models import User
from app.users.schemas import UserCreate, UserPublic
from app.users.service import UserService

router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.post("", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, session: SessionDep):
    service = UserService(session)
    return service.create_user(data)


@router.get("/me", response_model=UserPublic)
def get_me(user: User = Depends(get_current_user)):
    return user


@router.get("/{user_id}", response_model=UserPublic)
def get_user(user_id: int, session: SessionDep):
    service = UserService(session)
    return service.get_user(user_id)
