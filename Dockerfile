FROM python:3.6.1-slim

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt -r test-requirements.txt

RUN nosetests
