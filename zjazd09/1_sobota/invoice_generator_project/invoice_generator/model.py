import json
from pathlib import Path

from pydantic import BaseModel


class Company(BaseModel):
    name: str
    address1: str
    postal_code: str
    city: str
    nip: str
    bank: str
    account: str


class InvoiceConfig(BaseModel):
    company: Company



def load(config_filepath: str | Path) -> InvoiceConfig:
    config = json.load(open(config_filepath, encoding="UTF-8"))
    return InvoiceConfig(**config)
