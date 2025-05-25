import requests
import typer


def translate(text: str):
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiN2VlN2U2MjQtNTM1ZS00MjdmLWIzMjMtNzFlODVjMTJjNjliIiwidHlwZSI6ImFwaV90b2tlbiJ9.IpULU6VRZAOLuhhfV0Mg0bA7kS3ciiCs56POikR7gNs"}
    print(text)
    url = "https://api.edenai.run/v2/translation/automatic_translation"
    payload = {
        "providers": "microsoft",
        "source_language": "kr",
        "target_language": "pl",
        "text": text,
    }

    response = requests.post(url, json=payload, headers=headers)

    result = response.json()
    print(result['microsoft']['text'])


if __name__ == '__main__':
    typer.run(translate)