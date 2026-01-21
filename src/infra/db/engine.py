from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.ECHO_SQL,
    future=True,
)

AsyncSessionLocal = sessionmaker(  # type: ignore
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
