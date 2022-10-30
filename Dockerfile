FROM python:3.9-alpine
ARG BUILD_DEPS=".build-deps"
COPY . /app
WORKDIR /app
RUN apk add --no-cache --update --virtual ${BUILD_DEPS} \
    build-base \
    musl-dev \
    libffi-dev \
    python3-dev \
    openssl-dev \
    openssh-client \
 && pip install .
CMD ["raspi_mqtt_client"]