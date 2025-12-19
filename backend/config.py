from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database Settings
    db_name: str = "PashaServe"
    db_host: str = "localhost"
    db_port: int = 5432
    postgresql_username: str


    # API Keys
    power_automate_api_key: str
    postgresql_password: str

    # Application
    app_name: str = "Resturant CRM"
    debug: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = False # DB_HOST and db_host both work


# Create instance
settings = Settings()