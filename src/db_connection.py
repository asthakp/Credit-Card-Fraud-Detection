from sqlalchemy import create_engine
from src.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

def get_engine():
    engine = create_engine(
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    )
    return engine