import os
import sqlite3
import tempfile
import unittest

from database import get_monthly_summary


class TestDatabaseMonthlySummary(unittest.TestCase):

    def test_get_monthly_summary_basic(self):
        # Create a temporary sqlite database file
        fd, db_path = tempfile.mkstemp(suffix='.db')
        os.close(fd)
        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            # Create table including date column
            cur.execute(
                """
                CREATE TABLE expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    category TEXT,
                    notes TEXT,
                    date TEXT
                )
                """
            )
            # Insert sample rows across months
            cur.execute("INSERT INTO expenses (amount, category, notes, date) VALUES (?, ?, ?, ?)", (10.0, 'Food', '', '2026-08-05'))
            cur.execute("INSERT INTO expenses (amount, category, notes, date) VALUES (?, ?, ?, ?)", (20.0, 'Transport', '', '2026-08-07'))
            cur.execute("INSERT INTO expenses (amount, category, notes, date) VALUES (?, ?, ?, ?)", (5.0, 'Food', '', '2026-07-30'))
            conn.commit()
            conn.close()

            rows = get_monthly_summary('2026', '08', db_path=db_path)
            # Convert to dict for easier assertions
            d = {cat: total for cat, total in rows}
            self.assertIn('Food', d)
            self.assertIn('Transport', d)
            self.assertAlmostEqual(d['Food'], 10.0)
            self.assertAlmostEqual(d['Transport'], 20.0)
        finally:
            os.remove(db_path)


if __name__ == '__main__':
    unittest.main()
