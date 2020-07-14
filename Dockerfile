FROM python:3.7
MAINTAINER gt401@cam.ac.uk

RUN mkdir /websitedjc
COPY requirements.txt .

RUN pwd
RUN ls -la /websitedjc

RUN python3 -m venv /opt/venv 
RUN ls -la 
RUN . /opt/venv/bin/activate && pip3 install -r requirements.txt

COPY . /websitedjc
WORKDIR /websitedjc

EXPOSE 8000

CMD . /opt/venv/bin/activate && exec python3 manage.py runserver 0.0.0.0:8000
