FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install main API dependencies
RUN make install-platform-dependencies

# install plugin dependencies
RUN make install-plugin-dependencies

# Set the entry point to start plugins and the main API
CMD ["start.sh"]
