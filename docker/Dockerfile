FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY *.py /app/

ADD index.json /app/index.json


USER root
RUN echo 'alias search="python /app/app.py"' >> ~/.bashrc


CMD ["bash"]