import click


@click.command
@click.option("--text")
def translate(text: str):
    print(text)


if __name__ == '__main__':
    translate()