# Change: Scaffold Initial Application

## Why
プロジェクトの開始にあたり、開発の基盤となるアプリケーション構造、依存関係管理、データベース環境、およびテスト基盤を確立する必要があるため。
ユーザーの要望である「CLIとWeb APIの両方から利用可能なユースケースの分離」を実現するためのアーキテクチャを導入する。

## What Changes
- **プロジェクト構成**: `uv` を用いたPythonプロジェクトの初期化。
- **アーキテクチャ**: レイヤードアーキテクチャ（またはオニオンアーキテクチャ）を採用し、Core（ユースケース・ドメイン）、Infra（DB）、Interface（CLI/API）を分離。
- **Web API**: FastAPIを用いたAPIサーバーの雛形作成。
- **CLI**: Clickを用いたCLIツールの雛形作成。
- **Database**: PostgreSQL (PostGIS) のDocker Compose設定、SQLModel/Alembicによるマイグレーション構成。
- **Config**: Pydantic Settingsによる環境変数管理。
- **Testing/Linting**: pytest, ruff, black, mypy の設定。
- **Task Runner**: 開発効率化のための `Makefile` 追加。

## Impact
- 新規ファイル群の追加 (`src/`, `tests/`, `pyproject.toml`, `docker-compose.yml`, `alembic.ini` 等)
- 開発フローの確立（ローカルDB起動、マイグレーション実行、テスト実行の手順化）
