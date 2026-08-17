import tkinter as tk
from tkinter import messagebox

from database import insert_expense


class ExpenseForm:

    def __init__(self, parent):

        self.window = tk.Toplevel(parent)
        self.window.title("Add Expense")
        self.window.geometry("400x300")
        self.window.configure(bg="white")

        self.create_form()

    def create_form(self):

        tk.Label(
            self.window,
            text="Amount",
            bg="white",
            fg="black"
        ).pack(pady=(20, 5))

        self.amount_entry = tk.Entry(self.window, width=30)
        self.amount_entry.pack()

        tk.Label(
            self.window,
            text="Category",
            bg="white",
            fg="black"
        ).pack(pady=(15, 5))

        self.category_entry = tk.Entry(self.window, width=30)
        self.category_entry.pack()
        self.category_entry.insert(0, "Food")

        tk.Label(
            self.window,
            text="Notes",
            bg="white",
            fg="black"
        ).pack(pady=(15, 5))

        self.notes_entry = tk.Entry(self.window, width=30)
        self.notes_entry.pack()

        tk.Button(
            self.window,
            text="Save Expense",
            command=self.save_expense
        ).pack(pady=25)

    def save_expense(self):

        amount = self.amount_entry.get()
        category = self.category_entry.get()
        notes = self.notes_entry.get()

        insert_expense(amount, category, notes)

        messagebox.showinfo(
            "Expense Saved",
            "Your expense has been saved successfully!"
        )

        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)