import json
from pathlib import Path

from pydantic import BaseModel


class Company(BaseModel):
    name: str
    postal_code: str = ""
    city: str = ""
    address: str = ""
    nip: str = ""
    regon: str = ""


class Account(BaseModel):
    bank_name: str
    number: str
    currency: str


class Invoice(BaseModel):
    no_this_month: int
    company: Company
    payment_method: str
    payment_period: int


class Item(BaseModel):
    name: str
    net: float
    tax: float


class InvoiceConfig(BaseModel):
    company: Company
    account: Account
    invoice: Invoice
    items: list[Item]



def load(config_filepath: str | Path) -> InvoiceConfig:
    config = json.load(open(config_filepath, encoding="UTF-8"))
    return InvoiceConfig(**config)


def gen_schema():
    with open("schema.json", "w+") as schema_file:
        schema_file.write(json.dumps(InvoiceConfig.model_json_schema(), indent=4))


if __name__ == '__main__':
    gen_schema()
