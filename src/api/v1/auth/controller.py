from fastapi import APIRouter, HTTPException, Request

from src.lib.exceptions import RegistrationError
from src.api.v1.auth.dtos.registration import RegistrationDTO
from src.apps.user.dto import UserBaseDTO
from src.apps.auth.dependends.service import IAuthService


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/registration", response_model=UserBaseDTO)
async def registration(dto: RegistrationDTO, service: IAuthService, request: Request):
    """
    controller for registration user
    """
    try:
        return await service.registration(dto)
    except (RegistrationError, ValueError) as e:
        raise HTTPException(status_code=400, detail=str(e))
