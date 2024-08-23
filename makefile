install-platform-dependencies:
	pip install -r requirements.txt

download-plugins:
	python scripts/download_plugins.py

install-plugin-dependencies:
	python scripts/install_plugin_dependencies.py

docker-build-base:
	docker build -t plugin-platform-base:latest .

docker-push-base:
	docker tag plugin-platform-base:latest ghcr.io/dasiths/plugin-platform-base:latest
	docker push ghcr.io/dasiths/plugin-platform-base:latest

start:
	exec python scripts/start_all.py

start-full: install-platform-dependencies download-plugins install-plugin-dependencies start
