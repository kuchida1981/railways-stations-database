import click

from src.core.usecases.get_info import GetSystemInfo


@click.command()
def info() -> None:
    """Get system info."""
    usecase = GetSystemInfo()
    result = usecase.execute()
    click.echo(f"Version: {result.version}")
    click.echo(f"Status: {result.status}")
