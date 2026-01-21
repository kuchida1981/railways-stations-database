from pydantic import BaseModel


class SystemInfo(BaseModel):
    version: str
    status: str


class GetSystemInfo:
    def execute(self) -> SystemInfo:
        return SystemInfo(version="0.1.0", status="operational")
