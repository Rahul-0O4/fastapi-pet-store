## For creating a table and run this code just for once
import sqlite3

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("Table created successfully")
