  
FROM python:3.7-slim

MAINTAINER IGM Erwin "igmerwina@gmail.com"

RUN python -m pip install --upgrade pip

ENV LC_ALL=en_CA.UTF-8
ENV LANG=en_CA.UTF-8
ENV LANGUAGE=en_CA.UTF-8

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY  . .

EXPOSE 5000

CMD ["python","app.py"]
