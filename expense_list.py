import tkinter as tk
from tkinter import ttk

from database import get_expenses


class ExpenseList:

    def __init__(self, parent):

        self.window = tk.Toplevel(parent)
        self.window.title("Expenses")
        self.window.geometry("500x400")

        self.create_table()

    def create_table(self):

        expenses = get_expenses()

        self.tree = ttk.Treeview(
            self.window,
            columns=("Amount", "Category", "Notes"),
            show="headings"
        )

        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Notes", text="Notes")

        self.tree.column("Amount", width=100)
        self.tree.column("Category", width=150)
        self.tree.column("Notes", width=250)

        for expense in expenses:
            id, amount, category, notes = expense

            self.tree.insert(
                "",
                "end",
                values=(amount, category, notes)
            )

        self.tree.pack(fill="both", expand=True)