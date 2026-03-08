from flask import Blueprint, render_template, request, flash
import sqlite3

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather-data')
def weather_data():
    try:
        conn = sqlite3.connect('instance/database.db')
        cursor = conn.cursor()

        # Fetch available locations for the UI filter
        cursor.execute("SELECT DISTINCT location FROM WeatherData ORDER BY location")
        locations = [row[0] for row in cursor.fetchall()]

        selected_location = request.args.get('location', 'all')

        # If a specific location is requested, filter by it
        if selected_location and selected_location != 'all':
            cursor.execute("SELECT * FROM WeatherData WHERE location = ? ORDER BY timestamp", (selected_location,))
        else:
            cursor.execute("SELECT * FROM WeatherData ORDER BY timestamp")
        
        weather_records = cursor.fetchall()

    except sqlite3.Error as e:
        flash(f"Error fetching weather data: {str(e)}", "danger")
        weather_records = []
        locations = []
        selected_location = 'all'

    finally:
        conn.close()

    return render_template(
        'weather-data.html',
        weather_records=weather_records,
        locations=locations,
        selected_location=selected_location
    )
