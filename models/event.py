from typing import Optional, List

from bson import ObjectId
from pydantic import BaseModel, Field


class Event(BaseModel):
    """
    Event model
    """
    id: Optional[ObjectId] or None = Field(default=None, alias='_id')
    name: str
    description: Optional[str] = None
    date: str
    organizator: Optional[ObjectId] = None

    model_config = {
        "arbitrary_types_allowed": True,
    }
