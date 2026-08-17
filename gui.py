import tkinter as tk

from expense_form import ExpenseForm
from expense_list import ExpenseList


class ExpenseTrackerApp:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Yesh's Expense Tracker")
        self.window.geometry("500x350")

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
        self.welcome_label.pack(pady=40)

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