"""Handlers for Geo"""

from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

import requests
from fastapi import APIRouter, Depends, HTTPException

from config.app_config import YANDEX_GEO_API
from src.api.actions.geo_crud import create_geo_for_address, show_geo_for_address
from src.api.schemas.geo_schemas import GeoCreate, GeoShow
from src.db.session import get_db

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

logger = getLogger(__name__)
geo_router = APIRouter(prefix="/geo", tags=["GEO_CODER"])

ADDRESS_REQUEST = f"https://geocode-maps.yandex.ru/1.x/?apikey={YANDEX_GEO_API}&geocode="
ADDRESS_PARAMS = "&lang=ru_RU&results=1&format=json"


@geo_router.post("/get_geopoints", response_model=GeoShow)
async def get_geopoints(
        body: GeoCreate,
        db: AsyncSession = Depends(get_db),
) -> GeoShow | None | HTTPException:
    """Rout to show geo coordinates"""
    geo_exist = await show_geo_for_address(body, db)
    if geo_exist is not None:
        return geo_exist
    try:
        response = await request_for_api(body.address)
        geo_created = await create_geo_for_address(response, db)
        if geo_created is not None:
            return geo_created

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "status": 500,
                "data": None,
                "details": "Invalid address",
                "description": "Geocoder cannot be get geo points for this address",
            },
        ) from e


async def request_for_api(address_for_geo: str) -> GeoShow:
    """Request from yandex api"""
    current_address = "%20".join(address_for_geo.split(" "))
    query = f"{ADDRESS_REQUEST}{current_address}{ADDRESS_PARAMS}"
    request_quote = requests.get(query).json()
    geo_points = request_quote["response"]["GeoObjectCollection"]["featureMember"][-1]["GeoObject"]["Point"]["pos"]
    return GeoShow(address=address_for_geo, geo=geo_points)
