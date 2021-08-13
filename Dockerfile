FROM python:3.9

COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code
COPY . /code/