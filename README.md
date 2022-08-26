# :key: Flask auth google template

Flask app with Google auth login and postgres db

## :floppy_disk: Installation

```bash
python -m venv env
```

```bash
. env/scripts/activate
```

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## :wrench: Config

Create `.env` and `.env.db` files. Check the examples `.env.example` and `.env.db.example`

:globe_with_meridians: Google Auth credentials:

Create your app and obtain your `client_id` and `secret`:

```http
https://developers.google.com/workspace/guides/create-credentials
```
:construction: Before first run:

Run `docker-compose` :whale: to start the database server

```bash
docker compose -f "docker-compose.yml" up -d --build adminer db
```

and init the database with alembic:

```bash
alembic upgrade head
```

:key: How to create cert and key

For run the `option 2` or `option 3` you need a `cert.pem` and `key.pem`.  

Create a self-signed certificate with openssl:

```bash
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

## :runner: Run

### :1st_place_medal: Option 1

Run the database with docker and the app with flask using a cert adhoc.

- Database:

```bash
docker compose -f "docker-compose.yml" up -d --build adminer db
```

- Flask app:

```bash
flask --debug run --cert=adhoc
```

### :2nd_place_medal: Option 2

Run the database with docker and the app with flask using your certificate.

- Database:

```bash
docker compose -f "docker-compose.yml" up -d --build adminer db
```

- Flask app:

```bash
flask --debug run --cert=cert.pem --key=key.pem
```

### :3rd_place_medal: Option 3

Run the database and the flask app with docker. This option use a cert and key.  
In this option Flask run over gunicorn.

- Database and flask app:

```bash
docker compose -f "docker-compose.yml" up -d --build
```

## :pushpin: Features

- [x] Google Auth login
- [x] Sign up new users
- [x] Bootstrap
- [x] Flask
