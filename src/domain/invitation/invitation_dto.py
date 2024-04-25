from datetime import date

from pydantic import BaseModel


class InvitationBaseDTO(BaseModel):
    code: str
    at_valid: date
    status: str = "active"


class GetInvitationListDTO(InvitationBaseDTO):
    pass


class InvitationCreateDTO(InvitationBaseDTO):
    pass


class InvitationCheckCodeDTO(InvitationBaseDTO):
    pass
