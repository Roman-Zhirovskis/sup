from src.lib.exceptions import RegistrationError, AlreadyExistError
from src.api.v1.auth.dtos.registration import RegistrationDTO
from src.apps.user.depenends.repository import IUserRepository
from src.apps.user.entity import UserEntity
from src.apps.email.service import EmailService


class AuthService:

    def __init__(self, repository: IUserRepository):
        self.user_repository = repository
        self.email_service = EmailService()

    def _generate_confirm_link(self, user):
        domain = 'http://localhost:8000'
        link = f'{domain}/confirm/'
        return link

    async def registration(self, dto: RegistrationDTO):
        # TODO получить ссылку для регистрации и проверять, активна ли эта ссылка
        ragistration_data = dto.model_dump()
        ragistration_data.pop('password2')
        user_entity = UserEntity(**ragistration_data)
        try:
            user = await self.user_repository.create(user_entity)
            link = await self._generate_confirm_link(user)
            await self.email_service.send_message(user_entity.email, subject='confirmation link', ms=link)
            return user
        except AlreadyExistError as e:
            raise RegistrationError(e)

    async def invite(self, dto):
        print(dto)