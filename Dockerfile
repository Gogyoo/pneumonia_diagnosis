FROM python:3.10-buster

ADD pneumonia /pneumonia
COPY Makefile /Makefile
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn app.simple:app --host 0.0.0.0
