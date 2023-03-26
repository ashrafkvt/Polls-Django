FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /project

COPY ./requirements.txt /project/
RUN pip install -r /project/requirements.txt
RUN apt-get install postgresql-client

COPY . /project/

