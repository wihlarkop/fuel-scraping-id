from functools import lru_cache

from httpx import Client, Headers
from selectolax.parser import HTMLParser

from schema import FuelResponse
from settings import settings


class BP:
    def __init__(self, client: Client):
        self.client = client
        self.base_url = settings.BP_URL
        self.headers = Headers({
            "User-Agent": settings.USER_AGENT
        })

    @lru_cache
    def get_fuel_price(self) -> list[FuelResponse]:
        res = self.client.get(url=self.base_url, headers=self.headers)

        html = HTMLParser(html=res.text)

        table = html.css_first("table")
        rows = table.css("tr")

        data: list[FuelResponse] = []
        for row in rows:
            cells = row.css("th, td")
            result = [cell.text().strip() for cell in cells]
            if result[0] != "Jenis Produk" and "JABODETABEK" != result[1]:
                data.append(FuelResponse(product_name=result[0], price=result[1]))
        return data
