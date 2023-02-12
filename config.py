import os


class Settings:
    DATABASE_PORT: str = os.environ.get('DATABASE_PORT', 5432)
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD', '123456')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER', 'postgres')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB', 'moneytransfer')
    POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST', 'localhost')
    POSTGRES_HOSTNAME: str = os.environ.get('POSTGRES_HOSTNAME', 'localhost')

    class Config:
        env_file = './.env'

    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{DATABASE_PORT}/{POSTGRES_DB}'

settings = Settings()