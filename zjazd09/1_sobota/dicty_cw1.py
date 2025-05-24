import json

config = {
  "company": {
    "name": "QA Michał Szajkowski",
    "address1": "Blabla",
    "postal_code": "01-234",
    "city": "Warszawa",
    "nip": "123456789",
    "bank": "Santander Bank Polska",
    "account": "12 1234 1232"
  },
  "items": [
      {
          "name": "Poprowadzenie zajęć w miesiącu maj 2025",
          "net": 1000,
          "tax": 23
      },
      {
          "name": "Przygotowanie materiałów",
          "net": 42,
          "tax": 8
      }
  ]
}


print(json.dumps(config, indent=4))

print(config["company"]["name"])