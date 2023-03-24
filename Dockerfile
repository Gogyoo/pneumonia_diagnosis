FROM python:3.10-buster

COPY pneumonia/pneumonia
COPY Makefile/Makefile
COPY requirements.txt/requirements.txt
