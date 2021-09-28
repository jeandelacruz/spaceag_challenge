FROM python:3.8
LABEL maintainer="Docker SpaceAG Challenge"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . code
WORKDIR code

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install
