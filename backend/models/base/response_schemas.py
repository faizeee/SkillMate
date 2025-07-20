from pydantic import BaseModel

class ResponseMessage(BaseModel):
    success:bool = True
    message:str = "Operation Successful"
