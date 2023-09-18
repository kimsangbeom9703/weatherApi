import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))


class config:
    DB_TYPE: str = os.getenv("DB_TYPE")
    DB_USERNAME: str = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", 3306)
    DB_DATABASE: str = os.getenv("DB_DATABASE")

    DATABASE_URL = f"{DB_TYPE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

    SERVICE_KEY: str = os.getenv("SERVICE_KEY")
    API_URL: str = os.getenv('API_URL')

    GET_VERSION_URL = API_URL + str(os.getenv('FACT_WEATHER_VERSION_URL'))
    GET_VILAGE_URL = API_URL + str(os.getenv('GET_VILAGE_FACT_DATA_URL'))
    GET_ULTRA_URL = API_URL + str(os.getenv('GET_ULTRA_FACT_DATA_URL'))


settings = config()
