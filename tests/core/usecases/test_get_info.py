from src.core.usecases.get_info import GetSystemInfo


def test_get_system_info() -> None:
    usecase = GetSystemInfo()
    result = usecase.execute()
    assert result.version == "0.1.0"
    assert result.status == "operational"
