import tkinter as tk
from tkinter import messagebox

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

# Create the main window
window = tk.Tk()
window.title("Yesh's Expense Tracker") # Window title
window.geometry("500x350") # Window size
# Welcome message
welcome_label = tk.Label(
    window,
    text="Welcome to Yesh's Monthly Expense Tracker",
    font=("Georgia", 18)
)
welcome_label.pack(pady=40)

# Function for Add Expense window
def open_add_expense_window():
    add_window = tk.Toplevel(window)
    add_window.title("Add Expense")
    add_window.geometry("400x300")
    add_window.configure(bg="white")

    #Labels and entry fields for Amount
    tk.Label(
        add_window,
        text="Amount",
        bg="white",
        fg="black"
    ).pack(pady=(20, 5))

    amount_entry = tk.Entry(add_window, width=30)
    amount_entry.pack()
    

    #Labels and entry fields for Category
    tk.Label(
        add_window,
        text="Category",
        bg="white",
        fg="black"
    ).pack(pady=(15, 5))

    category_entry = tk.Entry(add_window, width=30)
    category_entry.pack()
    category_entry.insert(0, "Food")  # Pre-fill with "Food"

    #Labels and entry fields for Notes
    tk.Label(
        add_window,
        text="Notes",
        bg="white",
        fg="black"
    ).pack(pady=(15, 5))

    notes_entry = tk.Entry(add_window, width=30)
    notes_entry.pack()

    # Printing the expense details to the console when the "Save Expense" button is clicked
    def save_expense():
        amount = amount_entry.get()
        category = category_entry.get()
        notes = notes_entry.get()

        print("Expense Saved in the file!")
        print(f"Amount: {amount}")
        print(f"Category: {category}")
        print(f"Notes: {notes}")

        cursor.execute(
        """
        INSERT INTO expenses (amount, category, notes)
        VALUES (?, ?, ?)
        """,
        (amount, category, notes)
        )
        connection.commit()

        # Display a message box to confirm that the expense has been saved
        messagebox.showinfo("Expense Saved", "Your expense has been saved successfully!")

        # Clear the entry fields after saving
        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        notes_entry.delete(0, tk.END)

    tk.Button(
    add_window,
    text="Save Expense",
    command=save_expense
).pack(pady=25)

# Add Expense button in the main window
add_button = tk.Button(
    window,
    text="Add Expense",
    width=20,
    height=2,
    command=open_add_expense_window
)
add_button.pack()

# Function for View Expenses window
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    print(expenses)

    # Function for viewing expenses
    def view_expense_window():
        expenses_window = tk.Toplevel(window)
        expenses_window.title("Expenses")
        expenses_window.geometry("500x400")

        tk.Label(
            expenses_window,
            text="Amount      Category      Notes",
            font=("Arial", 12, "bold")
        ).pack(pady=10)
        
        for expense in expenses:
            id, amount, category, notes = expense

            tk.Label(
                expenses_window,
                text=f"{amount}    {category}    {notes}"
                #text=f"ID: {id}, Amount: {amount}, Category: {category}, Notes: {notes}"
            ).pack()

    view_expense_window()

# View Expenses button in the main window
view_button = tk.Button(
    window,
    text="View Expenses",
    width=20,
    height=2,
    command=view_expenses
)
view_button.pack()


# Keep the application running
window.mainloop()