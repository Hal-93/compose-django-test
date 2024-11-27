FROM python:3.11-slim

ENV PYTHONUBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
