import tkinter as tk

# Create the main window
window = tk.Tk()

# Window title
window.title("Expense Tracker")

# Window size
window.geometry("500x350")

# Welcome message
welcome_label = tk.Label(
    window,
    text="Welcome to Yesh's Monthly Expense Tracker",
    font=("Arial", 18)
)

welcome_label.pack(pady=40)

# Add Expense button
add_button = tk.Button(
    window,
    text="Add Expense",
    width=20,
    height=2
)

add_button.pack()

# Keep the application running
window.mainloop()