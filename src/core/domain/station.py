from typing import Optional

from sqlmodel import Field, SQLModel


class StationBase(SQLModel):
    name: str = Field(index=True)
    line_name: str


class Station(StationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
