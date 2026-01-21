## 1. Configuration
- [ ] 1.1 Install `pytest-cov` via `uv`
- [ ] 1.2 Update `pyproject.toml` with pytest coverage options (`--cov=src`, `--cov-fail-under=100`)
- [ ] 1.3 Configure coverage exclusions (e.g., `if __name__ == "__main__":`, `pragma: no cover`) in `pyproject.toml`
- [ ] 1.4 Update `Makefile` to include coverage commands (e.g., `test-cov`)

## 2. Verification
- [ ] 2.1 Run tests and verify coverage report generation
- [ ] 2.2 Ensure current code meets 100% coverage (add tests or exclusions if necessary)
- [ ] 2.3 Verify that adding uncovered code causes tests to fail
