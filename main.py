import tkinter as tk
from tkinter import messagebox



# Create the main window
window = tk.Tk()

# Window title
window.title("Yesh's Expense Tracker")

# Window size
window.geometry("500x350")

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

        print("Expense Saved!")
        print(f"Amount: {amount}")
        print(f"Category: {category}")
        print(f"Notes: {notes}")

        messagebox.showinfo("Expense Saved", "Your expense has been saved successfully!")

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

# Keep the application running
window.mainloop()