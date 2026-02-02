# Agent Instructions

## Language
- **Language**: Japanese (日本語)
- ユーザーとのやり取り、およびコミットメッセージやPRの記述には日本語を使用してください。

## Workflow: GitHub Flow & OpenSpec
1. **Issue Driven**: すべての変更は GitHub Issue から始まります。
2. **OpenSpec**: Issue の内容に基づき、OpenSpec (`openspec/`) でドキュメント（仕様・設計）を作成・更新します。
3. **Branching**: `main` ブランチからトピックブランチを作成します。
4. **Pull Request**: 実装後、PRを作成しレビューを経てマージします。

## Development Environment
- **Docker Compose**: API (`src/main_api.py`) と Database (PostGIS) は Docker Compose 上で動作させます。
- **Testing**: ローカルでのテスト実行は `uv run pytest` を基本としますが、CI/CD環境との整合性を意識してください。
