FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--certfile", "cert.pem", "--keyfile", "key.pem", "app.wsgi:app" ]