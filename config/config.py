from pydantic import BaseSettings


class Config(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOSTNAME: str

    class Config:
        env_file = '../.env'


settings = Config()