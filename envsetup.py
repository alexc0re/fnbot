import os
from dataclasses import dataclass

from dotenv import load_dotenv



@dataclass
class Credentials:
    load_dotenv()
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    AUTH_TOKEM: str = os.getenv("AUTH_TOKEN")
    DB_PASS: str = os.getenv("DB_PASSWORD")
    DB_USER: str = os.getenv("DB_USER")




