import sqlite3
import bcrypt  # used for password hashing
import os
from flask import current_app

# Path to the SQLite DB file used by this app
db = 'instance/database.db'


def init_db():
    """Create the database tables if they don't exist yet."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()

        # user table holds accounts
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            location TEXT NOT NULL
        );
        """)

        # notification_preferences stores per-user toggles
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notification_preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            weather_enabled INTEGER DEFAULT 0,
            pollution_enabled INTEGER DEFAULT 0,
            traffic_enabled INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE
        );
        """)

        conn.commit()

def add_user(username, email, password, location):
    """Insert a new user row with a bcrypt-hashed password."""
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO user (username, email, password, location)
        VALUES (?, ?, ?, ?);
        """, (username, email, hashed_password, location))
        conn.commit()

def get_user_by_username(username):
    """Return the user row for `username`, or None if not found."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, username, email, password, location 
        FROM user WHERE username = ?;
        """, (username,))
        return cursor.fetchone()

def check_password(username, password):
    """Verify a plaintext password against the stored bcrypt hash."""
    user = get_user_by_username(username)
    if not user:
        return False
    stored_password = user[3]
    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

def add_notification_preferences(user_id, weather, pollution, traffic):
    """Create a notification_preferences row for a user.

    Expects booleans or ints for weather/pollution/traffic.
    """
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO notification_preferences (user_id, weather_enabled, pollution_enabled, traffic_enabled)
        VALUES (?, ?, ?, ?)
        """, (user_id, int(weather), int(pollution), int(traffic)))
        conn.commit()

def get_notification_preferences(user_id):
    """Return the preference tuple (weather, pollution, traffic) for a user."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT weather_enabled, pollution_enabled, traffic_enabled 
        FROM notification_preferences WHERE user_id = ?;
        """, (user_id,))
        return cursor.fetchone()
