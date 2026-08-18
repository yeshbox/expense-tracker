import tkinter as tk
from tkinter import ttk
from datetime import date

from expense_form import ExpenseForm
from expense_list import ExpenseList
from database import get_monthly_summary


class ExpenseTrackerApp:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Yesh's Expense Tracker")
        self.window.geometry("500x400")

        self.create_main_window()

    # -----------------------------
    # Main Window
    # -----------------------------

    def create_main_window(self):

        self.welcome_label = tk.Label(
            self.window,
            text="Welcome to Yesh's Expense Tracker",
            font=("Georgia", 18)
        )
        self.welcome_label.pack(pady=30)

        self.add_button = tk.Button(
            self.window,
            text="Add Expense",
            width=20,
            height=2,
            command=self.open_add_expense_window
        )
        self.add_button.pack()

        self.view_button = tk.Button(
            self.window,
            text="View Expenses",
            width=20,
            height=2,
            command=self.open_view_expenses_window
        )
        self.view_button.pack()

        # Minimal change: add Monthly Summary button
        self.summary_button = tk.Button(
            self.window,
            text="Monthly Summary",
            width=20,
            height=2,
            command=self.open_monthly_summary_window
        )
        self.summary_button.pack(pady=(10, 0))

    # -----------------------------
    # Add Expense Window
    # -----------------------------

    def open_add_expense_window(self):
        ExpenseForm(self.window)

    # -----------------------------
    # View Expenses Window
    # -----------------------------

    def open_view_expenses_window(self):
        ExpenseList(self.window)

    # -----------------------------
    # Monthly Summary Window
    # -----------------------------

    def open_monthly_summary_window(self):
        win = tk.Toplevel(self.window)
        win.title("Monthly Expense Summary")
        win.geometry("500x400")

        today = date.today()
        current_year = today.year
        current_month = today.month

        # Year selector (last 10 years)
        years = [str(y) for y in range(current_year - 9, current_year + 1)]
        tk.Label(win, text="Year:").pack(pady=(10, 0))
        year_cb = ttk.Combobox(win, values=years, state="readonly")
        year_cb.set(str(current_year))
        year_cb.pack()

        # Month selector (1-12)
        months = [f"{m:02d}" for m in range(1, 13)]
        tk.Label(win, text="Month (01-12):").pack(pady=(10, 0))
        month_cb = ttk.Combobox(win, values=months, state="readonly")
        month_cb.set(f"{current_month:02d}")
        month_cb.pack()

        # Results tree
        tree = ttk.Treeview(win, columns=("Category", "Total"), show="headings")
        tree.heading("Category", text="Category")
        tree.heading("Total", text="Total")
        tree.column("Category", width=300)
        tree.column("Total", width=100, anchor="e")
        tree.pack(fill="both", expand=True, pady=(10, 0))

        def show_summary():
            for item in tree.get_children():
                tree.delete(item)

            year = year_cb.get()
            month = month_cb.get()
            rows = get_monthly_summary(year, month)

            for category, total in rows:
                tree.insert("", "end", values=(category, f"{total:.2f}"))

        tk.Button(win, text="Show Summary", command=show_summary).pack(pady=10)
