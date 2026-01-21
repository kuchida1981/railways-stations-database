# Railways Stations Database

日本国内の鉄道駅データベースを構築・維持するためのプロジェクト。

## Getting Started

### Prerequisites

- Python 3.11+
- uv
- Docker & Docker Compose

### Installation

```bash
make install
```

### Running the Application

**Web API:**
```bash
make run-api
# Access http://localhost:8000/docs
```

**CLI:**
```bash
make run-cli -- info
```

### Database

Start the database:
```bash
make db-up
```

Run migrations:
```bash
make migrate
```

### Testing

```bash
make test
```
