# Base image
FROM mcr.microsoft.com/devcontainers/python:3.11

ENV PATH="/root/.local/bin:$PATH"

# Install Poetry
RUN pipx install poetry \
    && poetry config virtualenvs.create false

# Set the working directory
WORKDIR /app

# Copy dependencies
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN poetry install

# Copy the source code
COPY . .
