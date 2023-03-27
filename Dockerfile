
FROM tensorflow/tensorflow:2.10.0


# COPY Makefile /Makefile

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY pneumonia /pneumonia
COPY setup.py /setup.py
RUN pip install .

CMD uvicorn pneumonia.api.fastapi:app --host 0.0.0.0 --port $PORT

