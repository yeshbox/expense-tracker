# Expense Tracker

A small desktop expense tracker built with Python, Tkinter and SQLite.

I built this as a hands-on project to explore how a simple idea moves from a requirement to a working application, including the interface, data model, persistence and a few iterations along the way.

## What it does

- Add and record expenses
- View recorded expenses
- Store expenses locally using SQLite
- Categorise expenses
- View monthly spending summaries
- Keep data locally on the user's machine

## Built with

- **Python**
- **Tkinter** for the desktop interface
- **SQLite** for local data storage

## Project structure

```text
expense-tracker/
├── main.py
├── gui.py
├── expense_form.py
├── expense_list.py
├── database.py
├── tests/
└── README.md
```

## What I explored

This project helped me get more comfortable with:

- Structuring a small application into separate modules
- Designing a simple database and working with SQLite
- Connecting a user interface to application logic
- Adding features to an existing application without breaking what already works
- Using Git and GitHub as part of the development process
- Using AI-assisted development while still reviewing and testing the resulting code

## Running locally

Clone the repository, install the required dependencies, and run:

```bash
python main.py
```

The SQLite database is created locally and is intentionally **not stored in the repository**.

## A small project, deliberately

This isn't intended to be a production financial application.

It started as a simple expense tracker and became a way to learn by building, changing things, breaking things and fixing them.

More experiments to come.
