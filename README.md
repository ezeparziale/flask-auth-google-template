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
docker compose -f "docker-compose.yml" up -d --build
```

and init the database with alembic:

```bash
alembic upgrade head
```

## :runner: Run

Database:

```bash
docker compose -f "docker-compose.yml" up -d --build
```

Flask app:

```bash
flask --debug run --cert=adhoc
```

## :pushpin: Features

- [x] Google Auth login
