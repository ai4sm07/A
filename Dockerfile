FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["python3","manage.py","runserver","0.0.0.0:8011"]
