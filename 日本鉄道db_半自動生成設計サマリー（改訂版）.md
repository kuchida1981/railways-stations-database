# 日本の鉄道データベース 半自動生成設計（改訂・引き継ぎ用）

## 目的

- 日本国内の **鉄道会社・路線・駅** を網羅したデータベースを構築する
- 人手による継続的メンテナンスを避ける
- **国土交通省（MLIT）データを一次ソース（baseline）** とし、
  - Web クローリング
  - 公式サイト
  - OpenStreetMap
  - AI による差分検出
 で最新情報を追跡する
- ただし **最終的な有効化は人間が承認**する「半自動」方式を採用

---

## 基本思想（重要）

- **UPDATE で上書きしない**
- 変更はすべて **履歴（イベント）として INSERT**
- 「最新」とは
  - *人が承認した中で effective_date / registered_at が最も新しいもの*
- AI は「正」を決めない
  - 差分候補の検出・分類・確信度算出のみを担当

---

## MLIT データの位置づけ

### MLIT N02 鉄道データの性質

- 路線中心のデータ（MultiLineString）
- 主な属性
  - N02_001: 鉄道区分コード
  - N02_002: 事業者種別コード
  - N02_003: 路線名
  - N02_004: 運営会社名
  - N02_005: 代表的な駅名（※駅マスタではない）

👉 **MLIT は「事実のスナップショット」**
👉 論理モデルの「正」とは切り離す

---

## データ取り込み方針（非常に重要）

### 原則

- `mlit_railway_raw` への取り込み時点では
  - **他のテーブルへは原則 INSERT しない**
- raw 取り込みと意味付け（正規化・差分解釈）を完全に分離する

### 例外（初回のみ）

- 初回インポート時は **baseline 構築** のため
  - companies
  - lines
  - railway_changes（baseline）
 へ自動 INSERT を行う

---

## テーブル設計（概要）

### 1. 生データ保持（意味を解釈しない）

```sql
mlit_railway_raw
- id
- railway_type_code (N02_001)
- operator_type_code (N02_002)
- line_name (N02_003)
- operator_name (N02_004)
- station_name (N02_005)
- geometry (MultiLineString, SRID 4326)
- source_version
- imported_at
```

- UPDATE しない
- 再インポート・将来検証に耐える

---

### 2. 論理モデル（DB 上の「正」）

#### companies
- company_id
- canonical_name
- railway_type_code
- operator_type_code

#### lines
- line_id
- company_id
- canonical_name
- geometry

#### stations
- station_id
- canonical_name
- latitude / longitude

#### alias 系
- company_aliases
- line_aliases
- station_aliases

---

### 3. 路線 × 駅（多対多）

```sql
line_stations
- line_id
- station_id
- station_number
- position_order
```

---

## MLIT と論理モデルの関係

### 方針

- **直接的な FK は張らない**
- MLIT は「外部観測事実」、論理モデルは「承認済み知識」

### マッピングテーブルで対応

#### mlit_company_map
- mlit_raw_id
- company_id
- confidence
- decided_by (auto / manual)

#### mlit_line_map
- mlit_raw_id
- line_id
- match_method (name / geometry / both)
- confidence

#### mlit_station_hint
- mlit_raw_id
- station_id
- hint_type (representative / nearby)
- distance_m
- confidence

👉 **弱結合・説明可能性を重視**

---

## 差分・履歴管理（中核）

### railway_changes

```sql
- change_id
- entity_type (company / line / station / line_station)
- entity_id
- change_type (baseline / new / rename / close / transfer)
- old_value (JSONB)
- new_value (JSONB)
- effective_date
- source (mlit / official / osm / ai)
- confidence
- is_approved
- approved_at / approved_by
- detected_at
```

- すべての変更はイベント
- 実体テーブルは「承認済みイベントの投影結果」

---

## 運用フロー（時系列）

### フェーズ0：初回構築（baseline）

1. MLIT 全件を `mlit_railway_raw` に投入
2. company / line を自動生成
3. `railway_changes (baseline, is_approved=true)` を生成

---

### フェーズ1：定期インポート（通常）

1. MLIT / Web / OSM / 公式サイトを取得
2. AI により差分候補を生成
3. `railway_changes` に **未承認レコード** を INSERT
4. 論理モデルは変更しない

---

### フェーズ2：人間レビュー

- 変更前 / 変更後
- 根拠 URL / 文言
- AI の confidence

を確認し、承認

---

### フェーズ3：反映

- 承認済みイベントを
  - companies
  - lines
  - stations
  - line_stations
へ反映

---

## AI の役割

- テキスト・HTML・PDF から事実候補を抽出
- 差分分類（new / rename / close …）
- confidence 算出
- レビュー用要約生成

❌ AI が正を決めない
✅ AI は「疑わしい変化」を列挙

---

## 重要な割り切り

- MLIT の駅名は駅マスタではない
- 廃止は DELETE しない（close イベント）
- 表記ゆれは alias で吸収
- 最新 = 承認済み最新

---

## この設計の強み

- MLIT 更新に耐える
- 誤検知の修正が容易
- 履歴がそのまま価値になる
- AI と人間の役割分担が明確
- API / 可視化 / GTFS 連携に拡張可能

---

## 他エージェントで具体化すべき論点

- 自動マッチングアルゴリズム（名前 + geometry）
- 差分検出ロジック（擬似コード / SQL）
- レビュー UI（CLI / Web）の最小構成
- 駅 ID の永続性ポリシー
