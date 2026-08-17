import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("expense_tracker.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        notes TEXT
    )
    """)

connection.commit()


def insert_expense(amount, category, notes):
    cursor.execute(
        """
        INSERT INTO expenses (amount, category, notes)
        VALUES (?, ?, ?)
        """,
        (amount, category, notes)
    )
    connection.commit()


def get_expenses():
    cursor.execute("SELECT * FROM expenses")
    return cursor.fetchall()