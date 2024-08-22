install-platform-dependencies:
	pip install -r requirements.txt

download-plugins:
	python scripts/download_plugins.py

install-plugin-dependencies:
	python scripts/install_plugin_dependencies.py

docker-build:
	docker build -t plugin-platform:latest .

docker-push:
	docker tag plugin-platform:latest ghcr.io/dasiths/plugin-platform:latest
	docker push ghcr.io/dasiths/plugin-platform:latest

start:
	python scripts/start_plugins.py &
	uvicorn api.main:app --host 0.0.0.0 --port 8000