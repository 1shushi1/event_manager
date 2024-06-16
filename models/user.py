from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class User(BaseModel):
    """
    User model
    """
    id: Optional[ObjectId] = Field(None, alias='_id')
    username: str
    password: str
    model_config = {
        "arbitrary_types_allowed": True,
    }
