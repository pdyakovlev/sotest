from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_title: str = 'Тестовое задание'
    desc: str = 'Описание'
    database_url: str = 'Здесь должна быть строка подключения бд'

    class Config:
        env_file = '.env'


settings = Settings()
