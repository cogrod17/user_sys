from fastapi import APIRouter
from v1.routes import friends, users, posts

router = APIRouter()

# router.include_router(auth.router, tags=['users'], prefix='/users')
router.include_router(users.router, tags=['Users'], prefix='/users')
router.include_router(friends.router, tags=[
                      'Friends'], prefix="/friends")
router.include_router(posts.router, tags=['Posts'], prefix='/posts')
