# Base image
FROM mcr.microsoft.com/devcontainers/python:3.11 AS base

# Install Poetry
RUN pipx install poetry \
    && poetry config virtualenvs.create false

# Set the working directory
WORKDIR /app

# Copy dependencies
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry install

# Production image
FROM base AS prod

# Copy the source code
COPY . .
