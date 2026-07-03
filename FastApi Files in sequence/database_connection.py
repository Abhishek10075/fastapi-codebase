from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Connect to SQLite database
conn = sqlite3.connect("my_database.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    completed BOOLEAN
)
""")

conn.commit()

# Home Route
@app.get("/")
def home():
    return {"message": "SQLite Database Connection is successful"}