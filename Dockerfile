FROM python:3.10-buster


# COPY Makefile /Makefile
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY pneumonia /pneumonia
COPY setup.py /setup.py
RUN pip install .

CMD uvicorn pneumonia.api.fastapi:app --host 0.0.0.0 --port $PORT
