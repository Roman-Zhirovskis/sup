from fastapi import APIRouter, HTTPException

from src.app.dependencies.services import IAuthService
from src.domain.auth.dto.registration import RegistrationDTO
from src.lib.exceptions import RegistrationError
from src.domain.user.user_dto import UserBaseDTO
from src.domain.user.user_entity import UserEntity

router = APIRouter(prefix="/auth", tags=["permissions"])


@router.post("/registration", response_model=UserBaseDTO)
async def registration(dto: RegistrationDTO, service: IAuthService):
    """
    controller for registration user
    """
    try:
        return await service.registration(dto)
    except (RegistrationError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))


