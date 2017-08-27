FROM ubuntu:latest
MAINTAINER Pavel Rybalko "paul.rybalko@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
VOLUME ["/code"]
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
WORKDIR /code
CMD gunicorn --bind 0.0.0.0:8080 wsgi:app
