FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code/house_server

COPY requirements.txt /code/house_server/

# # Build Postgres-binary from source required dependencies
# RUN apk add --no-cache --update \
#     --virtual .build-deps --no-cache postgresql-dev gcc \
#     python3 python3-dev gcc \
#     gfortran musl-dev \
#     libffi-dev openssl-dev\
#     build-base\
#     apk --purge del .build-deps

RUN apt-get update \  
  && apt-get install -y build-essential libpq-dev \  
  && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/house_server/

RUN chmod +x entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]