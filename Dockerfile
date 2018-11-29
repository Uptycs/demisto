FROM python:2.7

COPY ./requirements.txt /opt/requirements.txt

RUN pip install --no-cache-dir -r /opt/requirements.txt
