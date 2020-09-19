# Pull base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /home/mateusz/django_projects/m_portfolio

# install dependencies
COPY Pipfile Pipfile.lock /home/mateusz/django_projects/m_portfolio/
RUN pip install pipenv && pipenv install --system

# copy project
COPY . /home/mateusz/django_projects/m_portfolio/