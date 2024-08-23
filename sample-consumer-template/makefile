docker-build:
	docker build -t plugin-platform-consumer:latest .

docker-run:
	exec docker rm -f plugin-platform-consumer || true
	exec docker run -d -p 8000:8000 --name plugin-platform-consumer plugin-platform-consumer:latest
	exec docker logs -f plugin-platform-consumer
