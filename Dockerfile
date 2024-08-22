FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install main API dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download plugins and install their dependencies
RUN python scripts/download_plugins.py && python scripts/install_plugin_dependencies.py

# Set the entry point to start plugins and the main API
CMD ["bash", "-c", "python scripts/start_plugins.py && uvicorn api.main:app --host 0.0.0.0 --port 8000"]
