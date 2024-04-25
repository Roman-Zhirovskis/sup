from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from src.lib import Base


class InviteRegistrationModel(Base):
    """Модель приг

    :param id: идентификатор
    :param title: название митапа
    :param date: дата митапа
    :param color: цвет митапа
    :param users: пользователи, учавствующие в митапе
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "invite_registation"

    title: Mapped[str]
    finish_at: Mapped[datetime]
    code: Mapped[str]
    is_active: Mapped[bool]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))