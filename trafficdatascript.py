
import sqlite3
import csv



# Local DB path and CSV source
DATABASE = 'instance/database.db'
CSV_FILE = 'data/bay_area_traffic_data.csv'


def initialize_db():
   """Create TrafficData table (if missing) and load rows from the CSV."""
   conn = sqlite3.connect(DATABASE)
   conn.row_factory = sqlite3.Row
   cursor = conn.cursor()

   # Ensure the table exists
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS TrafficData (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       Timestamp TEXT NOT NULL,
       Route TEXT NOT NULL,
       TypeOfCollision TEXT NOT NULL,
       Description TEXT NOT NULL
   )
   ''')

   # Read the CSV and insert each row
   with open(CSV_FILE, 'r') as file:
       reader = csv.DictReader(file)
       for row in reader:
           timestamp = row.get('Timestamp')
           route = row.get('Route')
           collision_type = row.get('TypeOfCollision')
           description = row.get('Description')

           cursor.execute('''
           INSERT INTO TrafficData (Timestamp, Route, TypeOfCollision, Description)
           VALUES (?, ?, ?, ?)
           ''', (timestamp, route, collision_type, description))

   conn.commit()
   conn.close()
   print("Traffic CSV imported into the local database.")


# Run the script to populate the DB when executed directly
initialize_db()
