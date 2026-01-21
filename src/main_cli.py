import click

from src.cli.system import info


@click.group()
def cli() -> None:
    pass


cli.add_command(info)

if __name__ == "__main__":
    cli()
