from typing import List
from pydantic import BaseModel, Field


class GetResponseResourceModel(BaseModel):
    user_id: int = Field(alias='userId')
    id: int
    title: str
    body: str


class GetResponseResourceListModel(BaseModel):
    __root__: List[GetResponseResourceModel]
