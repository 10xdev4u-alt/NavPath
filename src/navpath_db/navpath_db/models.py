import sqlite3

def create_tables(db_conn):
    db_conn.execute("CREATE TABLE IF NOT EXISTS waypoints (id INTEGER PRIMARY KEY, x REAL, y REAL)")
