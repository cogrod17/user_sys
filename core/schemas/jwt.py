from pydantic import BaseModel


class DecodedToken(BaseModel):
    userId: int
    expiry: float
