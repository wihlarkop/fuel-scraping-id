from httpx import Client, Headers

from schema import FuelResponse
from settings import settings


class Shell:
    def __init__(self, client: Client):
        self.client = client
        self.base_url = settings.SHELL_URL
        self.headers = Headers({
            "User-Agent": settings.USER_AGENT
        })

    def get_fuel_price(self) -> list[FuelResponse]:
        pass
