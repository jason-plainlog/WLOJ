FROM alpine

RUN apk add python3
RUN pip3 install --upgrade pip
RUN pip install gunicorn flask pymongo

WORKDIR /app