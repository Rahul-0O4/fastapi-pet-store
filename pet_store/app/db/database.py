import sqlite3

DB_NAME = "pets.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        species TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)
    db.commit()
    db.close()
