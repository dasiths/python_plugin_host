FROM plugin-platform-base:latest

WORKDIR /app

# copy the plugin config for this consumer
COPY config.yaml .

# download plugins based on the config. yaml
RUN make download-plugins

# install plugin dependencies
RUN make install-plugin-dependencies

CMD ["make", "start"]
