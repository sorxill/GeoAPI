"""Main config for all app."""

import os

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ["DB_NAME"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
YANDEX_GEO_API = os.environ["YANDEX_GEO_API"]
