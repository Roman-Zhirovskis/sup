from fastapi import APIRouter
from .auth.register import router as auth
# Справочниковые контроллеры

router = APIRouter()

router.include_router(auth)
