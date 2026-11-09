from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional

class CryptoPriceSchema(BaseModel):
    symbol: str
    price: float

    @field_validator("price", mode="before")
    def parse_price(cls, value):
        """Garante a conversão segura de string/texto para float."""
        try:
            return float(value)
        except (ValueError, TypeError):
            raise ValueError(f"Preço inválido recebido da API: {value}")

class CryptoPriceDB(CryptoPriceSchema):
    id: int
    fetched_at: datetime

    class Config:
        from_attributes = True