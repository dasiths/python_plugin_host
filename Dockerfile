FROM python:3.12-slim

# install make
RUN apt-get update && apt-get install -y make

WORKDIR /app

COPY . .

# remove config.aml file from base as this will be consumer specific
RUN rm config.yaml

# remove plugins folder if it exists
RUN rm -rf plugins

# install platform dependencies
RUN make install-platform-dependencies

CMD ["make", "start"]
