from jwt import ExpiredSignatureError, PyJWTError, decode, encode, get_unverified_header
from src.config.jwt_config import config_token
from src.config.security import settings
from src.apps.auth.exceptions.token import InvalidSignatureError


class TokenService:

    def __init__(self) -> None:
        self.access_token_lifetime = config_token.ACCESS_TOKEN_LIFETIME
        self.refresh_token_lifetime = config_token.REFRESH_TOKEN_LIFETIME
        self.secret_key = settings.secret_key
        self.algorithm = settings.algorithm

    def _validate_token(self, token: str):
        token_info = get_unverified_header(token)
        if token_info["alg"] != self.algorithm:
            raise InvalidSignatureError("Key error")
        return token

    async def encode_token(self, payload: dict) -> str:
        return encode(payload, self.secret_key, self.algorithm)

    async def decode_token(self, token: str) -> dict:
        try:
            self._validate_token(token)
            return decode(token, self.secret_key, self.algorithm)
        except ExpiredSignatureError:
            raise ExpiredSignatureError("Token lifetime is expired")
        except PyJWTError:
            raise Exception("Token is invalid")
