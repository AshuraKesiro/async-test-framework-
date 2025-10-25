from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Класс конфигурации проекта.
    Позволяет удобно управлять настройками через .env файл или переменные окружения.
    """

    # Базовый URL для тестирования API
    base_url: str = "https://jsonplaceholder.typicode.com"

    # URL подключения к БД (демо, можно не использовать в тестах)
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/test_db"

    # Таймаут запросов
    request_timeout: int = 10

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Экземпляр настроек
settings = Settings()
