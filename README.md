# Rhythm Shop

E-commerce web site

## Installation

```bash
git clone https://github.com/chikundant/RhythmShop
```

## Usage

- Change _.env.prod_ file and set your values 

```python
DEBUG=0
SECRET_KEY=Your-value-here
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.mysql
SQL_DATABASE=postgrtesql
SQL_USER=postgrtesql
SQL_PASSWORD=postgrtesql
SQL_HOST=127.0.0.1
SQL_PORT=3306

EMAIL_HOST_USER=Your-email
EMAIL_HOST_PASSWORD=Your-password
```

Then run code using docker

```python
docker-compose build
```
```python
docker-compose up
```
