#!/bin/bash

set -e

# Ensure containerWorkspaceFolder is set
if [ -z "$containerWorkspaceFolder" ]; then
  echo "Error: containerWorkspaceFolder is not set."
  exit 1
fi
# Configure workspace as a safe git directory
git config --global --add safe.directory "$containerWorkspaceFolder"

# Use custom .bashrc
if [ -f .devcontainer/.bashrc ]; then
    cp .devcontainer/.bashrc /root/
else
  echo "Error: .devcontainer/.bashrc does not exist."
  exit 1
fi

# Install development dependencies
poetry config virtualenvs.in-project false
poetry install --with dev
# Install Jupyter kernel
poetry run python -m ipykernel install --user

# Install pre-commit hooks & their virtual environments
poetry run pre-commit install --install-hooks
