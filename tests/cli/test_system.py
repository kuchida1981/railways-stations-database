from click.testing import CliRunner

from src.main_cli import cli


def test_info_cli() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["info"])
    assert result.exit_code == 0
    assert "Version: 0.1.0" in result.output
    assert "Status: operational" in result.output
