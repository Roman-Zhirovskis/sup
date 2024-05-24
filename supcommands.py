import asyncio

from typer import Option, Typer

from commands.createuser.registeradmindto import CLICreateAdminDTO
from commands.createuser.repository import create_role, create_user
from src.apps.user.dto import CreateRoleDTO
from src.apps.user.entity import UserEntity


app = Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command(help="Create a new admin user")
def createsuperuser(
    name: str = Option(default="Roma", help="Имя пользователя"),
    surname: str = Option(default="Zhopa", help="Фамилия пользователя"),
    email: str = Option(..., help="Email адрес пользователя"),
    password: str = Option(..., prompt="Пароль пользователя", hide_input=True),
    name_telegram: str = Option(default="@Romazhopa", help="Имя пользователя в Telegram"),
    nick_telegram: str = Option(default="Andrey228", help="Никнейм пользователя в Telegram"),
    nick_google_meet: str = Option(default="kotenokV1", help="Никнейм пользователя в Google Meet"),
    nick_gitlab: str = Option(default="GitLabAdmin", help="Никнейм пользователя в GitLab"),
    nick_github: str = Option(default="GitHubAdmin", help="Никнейм пользователя в GitHub"),
):
    dto = CLICreateAdminDTO(
        name=name,
        surname=surname,
        email=email,
        password=password,
        name_telegram=name_telegram,
        nick_telegram=nick_telegram,
        nick_google_meet=nick_google_meet,
        nick_gitlab=nick_gitlab,
        nick_github=nick_github,
    )

    registration_data = dto.model_dump()
    registration_data["is_admin"] = True
    user_entity = UserEntity(**registration_data)

    asyncio.run(create_user(user_data=user_entity))


@app.command(help="Create a new role")
def createrole(name: str = Option(..., help="Название роли"), color: str = Option(..., help="Цвет роли")):
    dto = CreateRoleDTO(name=name, color=color)
    asyncio.run(create_role(dto))


if __name__ == "__main__":
    app()
