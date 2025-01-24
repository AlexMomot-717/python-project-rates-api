# Rates API

The application is an API tool for navigating rates.
It uses given parameters values to output daily average prices of navigation between two ports.

## Setup

### Docker

Start the application with:

```
make up
```

The dockerized application will be available at http://localhost:8000 or http://127.0.0.1:8000

### Local installation

### Setup:

Install dependencies:

```
poetry install
```

Create .env file following .env.example file info.

## Usage

Start the application with:

1. In a production environment:

```
make start
```
It will cause json response output as a line, without indentation.

2. In development environment:

```
poetry run flask --app rates_api.app:app --debug run
```

The application will be available at http://127.0.0.1:8000 in both way.


Get prices rates:

1. Bash:
Open new terminal window in application source and launch "curl" request with parameters:

```
curl "http://127.0.0.1:8000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=NLRTM"
```
Parameter values are just for example.

2. Browser's address bar:

```
http://127.0.0.1:8000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=NLRTM
```
Parameter values are just for example.
