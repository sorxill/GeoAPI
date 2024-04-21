"""Geo crud system - connect handlers with DAL's"""

from __future__ import annotations

from typing import TYPE_CHECKING

from src.api.schemas.geo_schemas import GeoCreate, GeoShow
from src.db.dals.geo_dals import GeoDAL

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def show_geo_for_address(body: GeoCreate, session: AsyncSession) -> GeoShow | None:
    async with session.begin():
        geo_dal = GeoDAL(session)
        geo = await geo_dal.dal_get_geo_by_address(
            address=body.address,
        )
        if geo:
            return GeoShow(
                address=geo.address,
                geo=geo.geo,
            )
        return None


async def create_geo_for_address(body: GeoShow, session: AsyncSession) -> GeoShow | None:
    async with session.begin():
        geo_dal = GeoDAL(session)
        geo_create = await geo_dal.dal_create_geo(
            address=body.address,
            geo=body.geo,
        )
        if geo_create:
            return GeoShow(
                address=geo_create.address,
                geo=geo_create.geo,
            )
        return None
