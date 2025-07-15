from typing import Self
from pydantic import BaseModel

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

    @classmethod
    def from_token(cls, token:str) -> Self:
        """
        Creates a TokenResponse instance from a given access token.
        """
        return cls(access_token=token)
    
# Explanation:
# cls: The first argument of a classmethod, `cls`, is implicitly the class itself.
#      You don't typically need to hint `cls` explicitly with `Type[SomeClass]`
#      unless you're dealing with very complex generic scenarios.
# -> Self: This is the modern and preferred way (Python 3.11+) to indicate
#          that the method returns an instance of the class on which the
#          method was called (i.e., `TokenResponse` in this case, or any
#          subclass if it were inherited).