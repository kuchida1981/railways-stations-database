## Context
CLIとWeb APIの両方から同じビジネスロジックを利用したい。また、将来的なスケーラビリティと保守性を考慮し、適切な関心の分離を行いたい。

## Goals
- ユースケース（ビジネスロジック）がインターフェース（Web/CLI）に依存しないこと。
- DB操作が抽象化されているか、少なくとも依存注入可能な状態であること。
- 型安全性（Type Hinting）を最大限活用すること。
- 開発者が容易に環境構築できること。

## Decisions

### Directory Structure
```
.
├── pyproject.toml
├── uv.lock
├── docker-compose.yml
├── .env.example
├── alembic.ini
├── Makefile
├── src/
│   ├── config.py         # Settings
│   ├── main_api.py       # API Entrypoint
│   ├── main_cli.py       # CLI Entrypoint
│   ├── core/             # Business Logic
│   │   ├── domain/       # Pydantic Models / Interfaces
│   │   └── usecases/     # Application Logic
│   ├── infra/            # Infrastructure
│   │   ├── db/           # Session, Engine
│   │   └── repositories/ # Data Access Implementation
│   ├── api/              # FastAPI Routers/Dependencies
│   └── cli/              # Click Commands
└── tests/
```

### Tech Stack Details
- **Package Manager**: `uv` - 高速で標準準拠。
- **ORM**: `SQLModel` - FastAPI/Pydanticとの相性が良く、SQLAlchemyのパワーも使える。
- **Migration**: `Alembic` - SQLModelと組み合わせて使用。
- **Async**: DBアクセスは `asyncpg` を使用し、FastAPIもCLIも非同期対応する（Clickは `anyio` または `asyncio` ラッパーを使用）。

### Testing
- `pytest` + `pytest-asyncio`
- DBテストには `testcontainers` または Docker Compose で立ち上げたDBを使用（今回はDocker Compose上のDBをテスト用DBとして使う方針で簡易化、または `pytest-postgresql` 等を検討するが、まずはシンプルに既存DB接続の別DBを使う形を想定）。

## Open Questions
- 特になし
