FROM python:3.9-buster

LABEL org.opencontainers.image.source https://github.com/sivakov512/python-microservice-template-example


ENV POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH" \
    POSTGRES_SSL_PATH=~/.postgresql/root.crt

RUN apt-get update \
    && apt-get install -y protobuf-compiler libssl-dev ca-certificates curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_VERSION="1.1.11" python - \
    && curl -L https://github.com/golang-migrate/migrate/releases/download/v4.15.1/migrate.linux-amd64.tar.gz | tar xvz \
    && mv migrate /usr/local/bin/migrate

RUN mkdir -p ~/.postgresql && \
    curl "https://storage.yandexcloud.net/cloud-certs/CA.pem" -o ~/.postgresql/root.crt && \
    chmod 0600 ~/.postgresql/root.crt


WORKDIR /usr/local/lib/example
COPY . .

RUN poetry install --no-dev \
	&& find proto -name "*.proto" | xargs -I {} python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. {}


CMD ["example"]
