# Data Science CookBook! 🚀

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![code style - Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![types - mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/python/mypy)

**AI & Data Science Sub-Chapter**. **Authors**: Tomás Urdiales ([tomas.urdialesbartolome@externel.be](mailto:tomas.urdialesbartolome@externel.be))

→ This repository demonstrates a framework to **easily** build professional and beautiful project documentation using just `python` and `markdown`! 🚀

All thanks to the open-source magic of: [`MkDocs`](https://www.mkdocs.org/), [`Material for MkDocs`](https://squidfunk.github.io/mkdocs-material/) and [`mkdocstrings`](https://mkdocstrings.github.io/) ! 🤓

You can check out the results here:
https://tomasurdiales.github.io/DataScienceCookBook/

> **Note:**
> this format is in the process of soon becoming the official directive/recommendation for all projects by the AI & Data Science Sub-Chapter.

---

## Getting started

###  Requirements

- [Poetry](https://python-poetry.org/)
- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- All other dependencies are listed in the `pyproject.toml` file and will be automatically handled by poetry.


### Setup

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