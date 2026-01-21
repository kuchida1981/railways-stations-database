# Project Context

## Purpose
日本国内の鉄道会社・路線・駅を網羅したデータベースを構築する。
人手による継続的なメンテナンス負荷を避け、国土交通省（MLIT）データをベースラインとしつつ、Webクローリング・公式サイト・OpenStreetMap・AIによる差分検出を用いて最新情報を追跡する。
最終的なデータの有効化は人間が承認する「半自動（Human-in-the-loop）」方式を採用し、高品質なデータを維持する。

## Tech Stack
- **Language**: Python
- **Frameworks**:
    - **CLI**: Click
    - **Web API**: FastAPI
    - **Package Manager**: uv
- **Architecture**: ユースケース層を分離し、CLIとWeb APIの両方から利用可能な構成とする。
- **Database**: PostgreSQL (PostGIS, JSONB必須) - 位置情報と柔軟なスキーマ対応のため
- **AI**: Gemini API (テキスト抽出、差分検出、要約生成)
- **Infrastructure**:
    - **Current**: Local (Docker Compose)
    - **Future**: Google Cloud Run + Cloud SQL

## Project Conventions

### Code Style
- **Formatter**: black
- **Linter**: ruff
- **Type Checking**: mypy
- **Configuration**: `pyproject.toml` で設定を一元管理

### Architecture Patterns
- **生データと論理モデルの分離**: インポートした生データ(`mlit_railway_raw`)と、アプリケーション上の「正」となる論理モデルを明確に分ける。
- **追記型履歴管理 (Event Sourcing-like)**: 既存レコードを `UPDATE` せず、変更はすべてイベント(`railway_changes`)として `INSERT` し、履歴を保持する。
- **Human-in-the-loop**: AIは差分の検出・分類・確信度の算出のみを行い、最終的な「正」の決定（承認）は人間が行う。

### Testing Strategy
- **純粋関数（正規化・差分判定）**: ユニットテストで網羅
- **DB関連**: スキーマテスト + 最小限のE2Eテスト
- **クローラー**: スナップショットテスト（HTML等のパース結果検証）
- **AI部分**: 出力の「期待形式（スキーマ）」のみをテストし、内容は問わない

### Git Workflow
- **Strategy**: Trunk-based development
- **Process**: Feature branch → Pull Request (PR)
- **Constraint**: DDL変更・マイグレーションは必ずPRによるレビューを経ること

## Domain Context
- **MLITデータの性質**: 国土交通省のデータは「事実のスナップショット」であり、必ずしも論理的な駅マスタの正解ではない。路線中心（MultiLineString）のデータ構造を持つ。
- **データ階層**: 事業者 (Company) -> 路線 (Line) -> 駅 (Station)
- **「最新」の定義**: 人間によって承認された変更イベントの中で、`effective_date`（発効日）が最も新しいもの。

## Important Constraints
- **No UPDATE Policy**: マスターテーブルへの直接的な `UPDATE` は禁止。
- **AIの役割**: AIは事実を決定しない。「疑わしい変化」を検出し、人間に提示するまでを担当する。
- **疎結合 (Weak Coupling)**: MLIT生データテーブルと論理モデルテーブルの間に直接的な外部キー制約（FK）を張らない。マッピングテーブルを介して紐付ける。

## External Dependencies
- 国土交通省 国土数値情報ダウンロードサービス (MLIT)
- OpenStreetMap (OSM)
- 各鉄道会社公式サイト
- AI Models (Gemini 等)
