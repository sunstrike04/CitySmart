# CitySmart
CS411 Fall 2024 CitySmart project

Quickstart
---------

Prerequisites:

- Python 3.8+ (3.11 recommended)
- pip

Setup (local development):

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Create the instance DB (the app will also initialize user tables on first run):

```bash
python trafficdatascript.py   # populates TrafficData
python -c "import app"     # will initialize the DB via `init_db()`
```

Run the app:

```bash
export FLASK_APP=app.py
flask run
```

Tests:

```bash
pytest -q
```

Secrets / environment variables
-------------------------------

This project expects sensitive values to be provided via environment variables. Create a `.env` file in the project root (this file is ignored by git) with the following entries for local development:

```
SECRET_KEY=your-flask-secret-key
WEATHER_API_KEY=your-weatherapi-key
```

After creating `.env`, start the app as shown above — the project uses `python-dotenv` to load those values in development.

Next recommended steps
- Add a `LICENSE` file if you want to publish this repository.
- Add any missing CI checks or code style tooling you prefer.

