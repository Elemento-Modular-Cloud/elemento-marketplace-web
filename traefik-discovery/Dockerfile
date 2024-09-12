FROM python:3.9-slim
LABEL org.opencontainers.image.source https://github.com/Elemento-Modular-Cloud/elemento-marketplace-web

WORKDIR /app

ARG HOMEPAGE_PATH
ARG TRAEFIK_ROUTE
ARG USER
ARG PASSWORD

COPY ./src /app
COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set environment variables
ENV HOMEPAGE_PATH=$HOMEPAGE_PATH
ENV TRAEFIK_ROUTE=$TRAEFIK_ROUTE
ENV USER=$USER
ENV PASSWORD=$PASSWORD

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
