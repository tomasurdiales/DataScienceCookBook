# AI & Data Science Sub-Chapter - Tomás Urdiales

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![code style - Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![types - mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/python/mypy)

**Authors: Tomás Urdiales**

Correspondence: tomas.urdialesbartolome@externel.be

---

# Getting Started

→ The best way to get familiarised with the codebase is to start at ...


##  Requirements

- [Poetry](https://python-poetry.org/)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- All other dependencies are listed in the `pyproject.toml` file and will be automatically handled by poetry.


## Setup

Configure and activate virtual environment:
```console
poetry env use /path/to/python3.11
poetry shell
```

Install dependencies:
```console
poetry install --with dev --sync
```

Install pre-commit hooks:
```console
pre-commit install
```