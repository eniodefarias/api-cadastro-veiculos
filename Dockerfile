
#estágio de construção
FROM python:3.11-slim-buster AS builder


RUN useradd -m -u 1000 -U -s /bin/sh app && usermod -aG sudo app


RUN apt-get update && \
    apt-get -y install curl gnupg2 logrotate tzdata libsqlite3-dev

ENV TZ="America/Sao_Paulo"
ENV APP_DIR /app
WORKDIR ${APP_DIR}

COPY setup.py ${APP_DIR}/
COPY version ${APP_DIR}/
COPY .pre-commit-config.yaml ${APP_DIR}/
COPY .coveragerc ${APP_DIR}/
# COPY src ${APP_DIR}/src
COPY pyproject.toml ${APP_DIR}/src/pyproject.toml

COPY ./logrotate_app /etc/logrotate.d/app


RUN mkdir -p /var/lib/logrotate/ && \
    mkdir -p /var/log/ && \
    touch /var/log/app.log && \
    touch /var/log/extrator.log && \
    touch /var/lib/logrotate/status && \
    chmod 644 /etc/logrotate.d/* && \
    chown -R app ${APP_DIR} && \
    chgrp -R app ${APP_DIR}

ENV PATH="/home/app/.local/bin:${PATH}"





COPY Procfile ./









COPY src ${APP_DIR}/src
COPY pyproject.toml ${APP_DIR}/src/pyproject.toml


RUN logrotate -d /etc/logrotate.d/app && \
    chown -R app /var/log && \
    chown -R app ${APP_DIR}

USER app



RUN \
    # echo "pip direct" && pip install pre-commit && \
    echo "pip direct" && pip install --upgrade pip && \
    echo "pip direct" && pip install -e '.[all]'


EXPOSE 8000


CMD \
    uvicorn veiculos-api.api.app:app --host 0.0.0.0 --port 8000 --reload --access-log --log-level debug \
 