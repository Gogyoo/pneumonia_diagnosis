<<<<<<< HEAD
=======

>>>>>>> 58e330e7f95ca95abc9c7cf7ff4da4b5bfdd1fb0
FROM tensorflow/tensorflow:2.10.0


# COPY Makefile /Makefile
<<<<<<< HEAD
=======

>>>>>>> 58e330e7f95ca95abc9c7cf7ff4da4b5bfdd1fb0
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

<<<<<<< HEAD
=======

>>>>>>> 58e330e7f95ca95abc9c7cf7ff4da4b5bfdd1fb0
COPY pneumonia /pneumonia
COPY setup.py /setup.py
RUN pip install .

CMD uvicorn pneumonia.api.fastapi:app --host 0.0.0.0 --port $PORT
<<<<<<< HEAD
=======

>>>>>>> 58e330e7f95ca95abc9c7cf7ff4da4b5bfdd1fb0
