from pydantic import BaseModel, field_validator


class FuelResponse(BaseModel):
    product_name: str
    price: str

    @field_validator("price")
    def clean_price(cls, v: str):
        return v.translate({ord('\xa0'): " "})
