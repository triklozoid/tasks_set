FROM python:2.7-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY test.py /code/
COPY date_calculation /code/date_calculation
COPY lru_cache /code/lru_cache
