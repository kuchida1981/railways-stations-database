from fastapi import FastAPI

from src.api.system import router as system_router

app = FastAPI(title="Railways Database API")

app.include_router(system_router, prefix="/api", tags=["system"])


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
