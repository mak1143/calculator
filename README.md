# Calculator

A desktop calculator built with Python and Tkinter featuring a dark theme,
4-column grid layout, and full arithmetic expression evaluation.

## Quick Start

```bash
# Install dependencies
uv sync

# Run the calculator
python cal-v1.py
```

## Usage

The calculator supports standard arithmetic operations:

| Button | Operation |
|--------|-----------|
| `+` | Addition |
| `-` | Subtraction |
| `×` | Multiplication |
| `÷` | Division |
| `%` | Percentage |
| `+/-` | Toggle sign |
| `AC` | Clear all |
| `.` | Decimal point |
| `=` | Evaluate expression |

Enter an expression (e.g. `(12 + 8) * 3`) and press `=` to evaluate.

## Project Structure

```
calculator/
├── cal-v1.py            # Main Tkinter calculator application
├── main.py              # Stub entry point (placeholder)
├── pyproject.toml       # Project config (Python ≥3.11)
├── uv.lock              # Dependency lockfile
├── README.md            # This file
└── AGENTS.md            # Agent instructions and project notes
```

## Configuration

- **Python**: ≥3.11
- **Dependencies**: managed with `uv` (see `pyproject.toml`)
- **UI**: Tkinter (built-in with Python; no extra install needed)

## Security Note

`cal-v1.py` uses `eval()` for expression evaluation. This is acceptable for
a local desktop calculator but should not be used in a networked or
multi-user context without input sanitization.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch and open a Pull Request
