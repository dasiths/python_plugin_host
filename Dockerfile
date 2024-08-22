FROM python:3.12-slim

# install make
RUN apt-get update && apt-get install -y make

WORKDIR /app

COPY . .

# install platform dependencies
RUN make install-platform-dependencies

CMD ["make", "start"]
