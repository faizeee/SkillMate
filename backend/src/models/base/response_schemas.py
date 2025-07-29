from pydantic import BaseModel


class ResponseMessage(BaseModel):
    """Default response model of API responses."""

    success: bool = True
    message: str = "Operation Successful"
