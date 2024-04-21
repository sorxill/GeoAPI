"""Base models for Geo"""

from pydantic import BaseModel, Field


class GeoCreate(BaseModel):
    address: str = Field(min_length=1)


class GeoShow(BaseModel):
    address: str = Field(min_length=1)
    geo: str
