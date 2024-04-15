from functools import lru_cache

from pydantic_settings import BaseSettings


@lru_cache
class Settings(BaseSettings):
    USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    BP_URL: str = "https://www.bp.com/id_id/indonesia/home/produk-dan-layanan/spbu/harga.html"
    SHELL_URL: str = "https://www.shell.co.id/in_id/pengendara-bermotor/bahan-bakar-shell/harga-bahan-bakar-shell.html"


settings = Settings()
