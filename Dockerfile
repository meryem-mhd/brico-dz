# syntax=docker/dockerfile:1
FROM python:3.8

WORKDIR /home/app

COPY ./requirements.txt /home/app/requirements.txt

RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache \
	pip install -r requirements.txt

COPY ./app /home/app

