FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code/house_server

COPY requirements.txt /code/house_server/

# Build Postgres-binary from source required dependencies
RUN apk add --no-cache --update \
    --virtual .build-deps --no-cache postgresql-dev gcc \
    python3 python3-dev gcc \
    gfortran musl-dev \
    libffi-dev openssl-dev\
    build-base\
    apk --purge del .build-deps

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/house_server/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]