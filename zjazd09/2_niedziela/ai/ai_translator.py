import requests
import typer


def translate(text: str, token: str):
    headers = {"Authorization": f"Bearer {token}"}
    url = "https://api.edenai.run/v2/translation/automatic_translation"
    payload = {
        "providers": "microsoft",
        "source_language": "en",
        "target_language": "pl",
        "text": text,
    }

    response = requests.post(url, json=payload, headers=headers)

    result = response.json()
    print(result['microsoft']['text'])


if __name__ == '__main__':
    typer.run(translate)