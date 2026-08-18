import sqlite3
from datetime import date

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("expense_tracker.db")
cursor = connection.cursor()

# Ensure the expenses table exists with a date column. For new DBs, date defaults to today.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        notes TEXT,
        date TEXT DEFAULT (date('now'))
    )
    """)
connection.commit()

# Migration: if an existing DB had an expenses table without a date column, add it,
# and populate existing rows with today's date. These assigned dates are assumed
# (not historical) and are used so monthly summaries work immediately.
cursor.execute("PRAGMA table_info(expenses)")
columns = [row[1] for row in cursor.fetchall()]
if 'date' not in columns:
    # Add the date column and set today's date for existing rows
    cursor.execute("ALTER TABLE expenses ADD COLUMN date TEXT")
    cursor.execute("UPDATE expenses SET date = date('now') WHERE date IS NULL")
    connection.commit()


def insert_expense(amount, category, notes):
    """
    Insert a new expense. Keeps the same signature for backward compatibility.
    The date column is set to today's date by SQLite's date('now') function.
    """
    cursor.execute(
        """
        INSERT INTO expenses (amount, category, notes, date)
        VALUES (?, ?, ?, date('now'))
        """,
        (amount, category, notes)
    )
    connection.commit()


def get_expenses():
    """
    Return expenses in the same shape the UI expects: (id, amount, category, notes).
    Do not include the date here to avoid changing existing UI code that unpacks
    four values.
    """
    cursor.execute("SELECT id, amount, category, notes FROM expenses")
    return cursor.fetchall()


def delete_expense(expense_id):
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )
    connection.commit()


def get_monthly_summary(year, month, db_path=None):
    """
    Return a list of (category, total) for the given year and month.
    Optionally operate on a separate DB file by passing db_path (used by tests).
    """
    month_str = f"{int(month):02d}"
    year_str = str(year)

    if db_path:
        # Use a separate connection for the provided database path
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT category, SUM(amount) as total
            FROM expenses
            WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?
            GROUP BY category
            ORDER BY total DESC
            """,
            (year_str, month_str)
        )
        rows = cur.fetchall()
        conn.close()
        return rows

    cursor.execute(
        """
        SELECT category, SUM(amount) as total
        FROM expenses
        WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?
        GROUP BY category
        ORDER BY total DESC
        """,
        (year_str, month_str)
    )
    return cursor.fetchall()
