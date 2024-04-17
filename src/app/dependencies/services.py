from typing import Annotated
from fastapi import Depends
from src.domain.auth.auth_service import AuthService


IAuthService = Annotated[AuthService, Depends()]
