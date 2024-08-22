install-platform-dependencies:
	pip install -r requirements.txt

download-plugins:
	python scripts/download_plugins.py

install-plugin-dependencies:
	python scripts/install_plugin_dependencies.py

docker-build: install-platform-dependencies download-plugins install-plugin-dependencies
	docker build -t plugin-platform:latest .

docker-run:
	docker run -p 8000:8000 --name plugin-platform plugin-platform:latest

docker-push:
	docker tag plugin-platform:latest ghcr.io/dasiths/plugin-platform:latest
	docker push ghcr.io/dasiths/plugin-platform:latest

start:
	python scripts/start_all.py