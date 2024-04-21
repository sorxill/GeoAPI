"""DAL file for Geo"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import select

from src.db.models.geo import Geo

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class GeoDAL:
    """Data Access Layer for operating task info."""

    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def dal_create_geo(
        self,
        address: str,
        geo: str,

    ) -> Geo:
        """DAL create address with geo"""
        new_geo = Geo(
            address=address,
            geo=geo,
        )
        self.db_session.add(new_geo)
        await self.db_session.commit()
        return new_geo

    async def dal_get_geo_by_address(self, address: str) -> Geo | None:
        """DAL show address and geo for address"""
        query = select(Geo).where(Geo.address == address)
        res = await self.db_session.execute(query)
        geo_row = res.fetchone()
        if geo_row is not None:
            return geo_row[0]
        return None
