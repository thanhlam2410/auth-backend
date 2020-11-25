FROM python:3.9.0-buster

WORKDIR /pyauth

COPY requirements.txt /pyauth/requirements.txt
COPY .env /pyauh/.env
COPY .flaskenv /pyauh/.flaskenv

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
RUN mkdir /pyauth/db

COPY . /pyauth

ENV FLASK_APP py_auth.py
RUN flask db upgrade
RUN flask seed run

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "py_auth:app"]