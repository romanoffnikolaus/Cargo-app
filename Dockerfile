FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /application
WORKDIR /application

RUN mkdir /application/static

RUN pip install -r requirements.txt