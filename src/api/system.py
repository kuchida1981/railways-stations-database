from fastapi import APIRouter

from src.core.usecases.get_info import GetSystemInfo, SystemInfo

router = APIRouter()


@router.get("/info", response_model=SystemInfo)
async def get_info() -> SystemInfo:
    usecase = GetSystemInfo()
    return usecase.execute()
