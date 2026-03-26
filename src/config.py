import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
MYSQL_DB = os.getenv("MYSQL_DB")