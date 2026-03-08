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

Next recommended steps
- Add a `LICENSE` file if you want to publish this repository.
- Add any missing CI checks or code style tooling you prefer.

