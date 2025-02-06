# Use Ubuntu as base image
FROM ubuntu:22.04

# Set environment variables to prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive \
    UV_CACHE_DIR=/root/.cache/uv

# Install system dependencies (with APT cache)
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    cmake \
    build-essential \
    g++ \
    tesseract-ocr \
    tesseract-ocr-nld \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    ca-certificates \
    git \
    libzbar0 \
    python3-tk \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Ensure Python 3.11 is the default version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Install uv (fast package manager) and verify installation
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Set working directory
WORKDIR /workspaces/unstructured_data

# Copy only core dependencies (to leverage Docker caching)
COPY requirements-core.txt /workspaces/unstructured_data/

# Create virtual environment and install dependencies inside it
RUN /root/.local/bin/uv venv /root/.venv && \
    /root/.local/bin/uv pip install -r /workspaces/unstructured_data/requirements-core.txt --system --python /root/.venv/bin/python

# Install ruff    
RUN /root/.local/bin/uv tool install ruff@latest
