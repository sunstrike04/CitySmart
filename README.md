
# CitySmart

CitySmart is a Flask-based web application that brings together weather, air pollution, and traffic data to help users explore environmental and transportation conditions across different locations.

The application combines external weather data with information stored in a relational database, providing a centralized dashboard for viewing city statistics.

## Features

- **User accounts:** Sign up, log in, and maintain a personalized location preference.
- **City dashboard:** View weather and environmental statistics for a selected location.
- **Weather integration:** Retrieve current weather conditions through an external API.
- **Environmental data:** Query stored weather and pollution measurements, including temperature, humidity, particulate matter, and ozone levels.
- **Traffic information:** Access traffic-related data through dedicated application routes.
- **Database integration:** Use SQL queries to retrieve and aggregate city data.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Jinja2 templates
- **Database:** SQLite, SQL
- **APIs:** External weather API
- **Other tools:** Git, pytest, GitHub Actions

## Project Structure

```text
CitySmart/
├── app.py                 # Main Flask application
├── config.py              # Application configuration
├── models.py              # Database and user operations
├── routes/                # Weather, traffic, pollution, and settings routes
├── templates/             # HTML templates
├── static/css/            # Stylesheets
├── data/                  # Project data
├── tests/                 # Tests
├── weather_api.py         # Weather API integration
├── trafficdatascript.py   # Traffic data initialization
└── requirements.txt       # Python dependencies
```

## How It Works

CitySmart uses Flask to handle application requests and render HTML templates.

After signing in, users can access a dashboard associated with their selected location. The backend retrieves weather information from an external API and queries locally stored environmental data.

SQL queries aggregate weather and pollution measurements to calculate statistics such as average temperature, humidity, particulate matter, and ozone levels.

The application organizes weather, traffic, pollution, and settings functionality into separate Flask blueprints.

## Technical Highlights

- Organized backend functionality into separate Flask route modules.
- Integrated external API data with locally stored relational data.
- Used SQL joins and aggregate functions to generate location-specific statistics.
- Implemented user authentication and session-based application behavior.
- Added automated tests and a GitHub Actions workflow.

## Background

Originally developed as part of CS 411 (Database Systems) at the University of Illinois Urbana-Champaign, Fall 2024.
