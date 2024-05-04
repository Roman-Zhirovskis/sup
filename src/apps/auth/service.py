from src.lib.exceptions import RegistrationError, AlreadyExistError
from src.api.v1.auth.dtos.registration import RegistrationDTO
from src.apps.user.entity import UserEntity
from src.apps.user.depenends.service import IUserService
from src.apps.auth.dependends.token_service import ITokenService


class AuthService:

    def __init__(self,  user_service: IUserService, token_service: ITokenService):
        self.user_service = user_service
        self.token_service = token_service

    async def registration(self, dto: RegistrationDTO):
        registration_data = dto.model_dump()
        registration_data.pop('password2')
        user_entity = UserEntity(**registration_data)
        try:
            return await self.user_service.create(user_entity, email_confirmation=True)
        except AlreadyExistError as e:
            raise RegistrationError(e)
