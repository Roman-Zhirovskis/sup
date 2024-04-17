from typing import Annotated
from fastapi import Depends

from src.infra.repositories.login_repository import LoginRepository
from src.infra.repositories.permission_repository import PermissionRepository
from src.infra.repositories.role_repository import RoleRepository
from src.infra.repositories.user_repository import UserRepository


IUserRepository = Annotated[UserRepository, Depends()]
IRoleRepository = Annotated[RoleRepository, Depends()]
IPermissionRepository = Annotated[PermissionRepository, Depends()]
ILoginRepository = Annotated[LoginRepository, Depends()]
IEmailRepository = []