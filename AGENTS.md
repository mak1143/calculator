# AGENTS.md

## Project

Calculator project with two implementations:
- **Python/Tkinter** — `cal-v1.py` (desktop GUI, dark theme, matches web calculator design)
- **Web** — `calculator-application/` (HTML/CSS/JS calculator)

## Key Files

| File | Role |
|---|---|
| `cal-v1.py` | Main Python calculator (Tkinter GUI) |
| `main.py` | Stub entry point — prints a greeting, not the real app |
| `pyproject.toml` | Project config, Python ≥3.11, `tk` dependency |
| `uv.lock` | Lockfile — use `uv` to install deps |
| `calculator-application/` | Web calculator (HTML + CSS + JS) |

## Setup

```bash
uv sync          # install deps (including tk)
```

## Running

- **Python calculator**: `python cal-v1.py` (launches Tkinter GUI)
- **Web calculator**: open `calculator-application/calculator.html` in a browser

## Notes

- `main.py` is a placeholder — the real Python entrypoint is `cal-v1.py`
- `cal-v1.py` uses `eval()` for expression evaluation (security consideration)
- `cal-v1.py` shares the same dark theme and 4-column grid layout as the web calculator
- `calculator-application/text.txt` is actually JavaScript (older web calc version), not plain text
- No test suite, CI, or linting config exists yet
- `tk` is listed in `pyproject.toml` but the code uses built-in `tkinter` (no PyPI `tk` import needed)
