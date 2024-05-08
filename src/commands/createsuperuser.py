import asyncio

from sqlalchemy.exc import IntegrityError
from typer import Option, Typer

from src.apps.user.models.user import UserModel
from src.config.database.session import db_helper


app = Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


async def create_user(user_data: dict):
    async with db_helper.get_db_session() as session:
        user = UserModel(**user_data)
        session.add(user)
        await session.commit()


@app.command(help="Create a new user")
def createsuperuser(
    email: str = Option(..., help="Email адрес для суперпользователя"),
    password: str = Option(..., prompt="Пароль суперпользователя", hide_input=True),
):
    userd_dto = {"password": password, "email": email}
    asyncio.run(create_user(user_data=userd_dto))


if __name__ == "__main__":
    app()
