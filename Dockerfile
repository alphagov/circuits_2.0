FROM python:3.10-slim-buster

LABEL version="1.0"
LABEL maintainer="Data Services"

COPY . /circuits
WORKDIR /circuits

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 *.py
RUN chmod 444 requirements.txt

ENV PORT 8080
ENV SERVICE_NAME 'GDS Circuits generator'

EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 circuits:app