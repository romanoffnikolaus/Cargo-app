FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /application

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /application

RUN mkdir /application/static
