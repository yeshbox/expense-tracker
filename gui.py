import tkinter as tk
from tkinter import ttk, messagebox

from database import connection, cursor


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

        self.add_window = tk.Toplevel(self.window)
        self.add_window.title("Add Expense")
        self.add_window.geometry("400x300")
        self.add_window.configure(bg="white")

        tk.Label(
            self.add_window,
            text="Amount",
            bg="white",
            fg="black"
        ).pack(pady=(20, 5))

        self.amount_entry = tk.Entry(self.add_window, width=30)
        self.amount_entry.pack()

        tk.Label(
            self.add_window,
            text="Category",
            bg="white",
            fg="black"
        ).pack(pady=(15, 5))

        self.category_entry = tk.Entry(self.add_window, width=30)
        self.category_entry.pack()
        self.category_entry.insert(0, "Food")

        tk.Label(
            self.add_window,
            text="Notes",
            bg="white",
            fg="black"
        ).pack(pady=(15, 5))

        self.notes_entry = tk.Entry(self.add_window, width=30)
        self.notes_entry.pack()

        self.save_button = tk.Button(
            self.add_window,
            text="Save Expense",
            command=self.save_expense
        )
        self.save_button.pack(pady=25)

    def save_expense(self):

        amount = self.amount_entry.get()
        category = self.category_entry.get()
        notes = self.notes_entry.get()

        cursor.execute(
            """
            INSERT INTO expenses (amount, category, notes)
            VALUES (?, ?, ?)
            """,
            (amount, category, notes)
        )

        connection.commit()

        messagebox.showinfo(
            "Expense Saved",
            "Your expense has been saved successfully!"
        )

        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)

    # -----------------------------
    # View Expenses Window
    # -----------------------------

    def open_view_expenses_window(self):

        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        self.expenses_window = tk.Toplevel(self.window)
        self.expenses_window.title("Expenses")
        self.expenses_window.geometry("500x400")

        self.tree = ttk.Treeview(
            self.expenses_window,
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