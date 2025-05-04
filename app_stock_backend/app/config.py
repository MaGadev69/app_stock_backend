from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    # Si esta linea esta habilitada, la variable DATABASE_URL se obtiene del entorno (NEON)
    # Si no, se obtiene de las variables de entorno DB_HOST, DB_PORT, DB_NAME, DB_USER y DB_PASSWORD (DELL)
    DATABASE_URL_ENV: str = os.getenv("DATABASE_URL")

    # Variables de entorno
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "postgres")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "password")

    @property
    def DATABASE_URL(self):
        if self.DATABASE_URL_ENV:
            return self.DATABASE_URL_ENV
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

# global
settings = Settings()
