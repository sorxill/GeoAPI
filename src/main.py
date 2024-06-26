"""Main endpoint."""

import uvicorn
from fastapi import FastAPI

from src.api.handlers.geo_handler import geo_router

geoapp = FastAPI(
    title="GeoAPI",
    description="Test API for test task",
)

geoapp.include_router(geo_router)


@geoapp.get("/", description="Ping APP", name="Get rout For Ping")
def start_answer() -> dict:
    """Check the tests and e.t.c."""
    return {
        "answer": "Success",
    }


if __name__ == "__main__":
    uvicorn.run("main:geoapp", host="0.0.0.0", reload=True)
