import sqlite3
from flask import Blueprint, render_template, request


traffic_bp = Blueprint('traffic', __name__)


def get_db_connection():
    """Open a connection to the instance DB and return it.

    Rows will be returned as sqlite3.Row objects so templates can access by name.
    """
    connection = sqlite3.connect('instance/database.db')
    connection.row_factory = sqlite3.Row
    return connection


@traffic_bp.route('/traffic-data')
def traffic_data():
   conn = get_db_connection()

   # Get distinct collision types for the filter UI
   collision_types_query = 'SELECT DISTINCT TypeOfCollision FROM TrafficData ORDER BY TypeOfCollision'
   collision_types = [row['TypeOfCollision'] for row in conn.execute(collision_types_query).fetchall()]

   selected_collision_type = request.args.get('type_of_collision', 'all')

   if selected_collision_type and selected_collision_type != 'all':
       query = 'SELECT * FROM TrafficData WHERE TypeOfCollision = ? ORDER BY Timestamp'
       traffic_records = conn.execute(query, (selected_collision_type,)).fetchall()
   else:
       query = 'SELECT * FROM TrafficData ORDER BY Timestamp'
       traffic_records = conn.execute(query).fetchall()

   conn.close()

   return render_template('traffic-data.html',
                          traffic_records=traffic_records,
                          collision_types=collision_types,
                          selected_collision_type=selected_collision_type)