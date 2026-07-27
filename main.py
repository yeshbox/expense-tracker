import tkinter as tk

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
    font=("Arial", 18)
)

welcome_label.pack(pady=40)

def open_add_expense_window():
    add_window = tk.Toplevel(window)
    add_window.title("Add Expense")
    add_window.geometry("400x300")
    add_window.configure(bg="white")

    tk.Label(
        add_window,
        text="Amount",
        bg="white",
        fg="black"
    ).pack(pady=(20, 5))

    tk.Entry(add_window, width=30).pack()

    tk.Label(
        add_window,
        text="Category",
        bg="white",
        fg="black"
    ).pack(pady=(15, 5))

    tk.Entry(add_window, width=30).pack()

    tk.Label(
        add_window,
        text="Notes",
        bg="white",
        fg="black"
    ).pack(pady=(15, 5))

    tk.Entry(add_window, width=30).pack()

    tk.Button(
        add_window,
        text="Save Expense"
    ).pack(pady=25)

# Add Expense button
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