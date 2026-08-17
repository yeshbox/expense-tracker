import tkinter as tk
from tkinter import ttk, messagebox

from database import get_expenses, delete_expense


class ExpenseList:

    def __init__(self, parent):

        self.window = tk.Toplevel(parent)
        self.window.title("Expenses")
        self.window.geometry("500x450")

        self.create_table()
        self.create_delete_button()

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
            expense_id, amount, category, notes = expense

            self.tree.insert(
                "",
                "end",
                iid=str(expense_id),
                values=(amount, category, notes)
            )

        self.tree.pack(fill="both", expand=True)

    def create_delete_button(self):

        tk.Button(
            self.window,
            text="Delete Selected Expense",
            command=self.delete_selected_expense
        ).pack(pady=10)

    def delete_selected_expense(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "No Expense Selected",
                "Please select an expense to delete."
            )
            return

        expense_id = selected[0]

        confirm = messagebox.askyesno(
            "Delete Expense",
            "Are you sure you want to delete this expense?"
        )

        if confirm:
            delete_expense(expense_id)
            self.refresh_table()

    def refresh_table(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        expenses = get_expenses()

        for expense in expenses:
            expense_id, amount, category, notes = expense

            self.tree.insert(
                "",
                "end",
                iid=str(expense_id),
                values=(amount, category, notes)
            )