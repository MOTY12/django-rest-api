# syntax=docker/dockerfile:experimental

FROM --platform=$BUILDPALATFORM python:3.10-alpine AS builder
EXPOSE 8000
WORKDIR /app

# Install systen dependencies
RUN apk update
RUN apk add \
    pkgconfig \
    gcc \
    musl-dev \
    bash \
    mariaDB-dev

# Install python dependencies

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . /app

# run server
ENTRYPOINT [ "python3" ]
CMD [ "manage.py", "runserver", "0.0.0:8000" ]