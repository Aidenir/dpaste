FROM python:3-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ADD manage.py /manage.py
ADD requirements.txt /requirements.txt
ADD dpaste /dpaste

RUN pip install -r /requirements.txt
RUN python manage.py makemigrations && python manage.py migrate

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
