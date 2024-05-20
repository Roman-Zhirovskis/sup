import re
from typing import Optional

from pydantic import BaseModel, EmailStr, constr, model_validator


class RegistrationDTO(BaseModel):
    name: constr(max_length=20)
    surname: constr(max_length=20)
    email: EmailStr
    password: constr(min_length=8)
    password2: constr(min_length=8)
    name_telegram: constr(max_length=50)
    nick_telegram: constr(max_length=50)
    nick_google_meet: constr(max_length=50)
    nick_gitlab: constr(max_length=50)
    nick_github: constr(max_length=50)
    role_id: Optional[int] = None

    @model_validator(mode="after")
    def code_validate(self):
        if self.password != self.password2:
            raise ValueError("password missmatch")
        reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, self.password)
        if not mat:
            raise ValueError(
                "password must contain minimum 8 characters, at least one capital letter, number and "
                "special character"
            )
        return self
