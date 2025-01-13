from pydantic import BaseModel
from datetime import datetime

class UserResponse(BaseModel):
    uname: str
    user_id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True