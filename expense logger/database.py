import sqlite3
from expense import Expense


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                amount REAL,
                category TEXT,
                date TEXT
            )
        """)
        self.connection.commit()

    def add_expense(self, expense):
        self.cursor.execute("""
            INSERT INTO expenses (title, amount, category, date)
            VALUES (?, ?, ?, ?)
        """, (expense.title, expense.amount, expense.category, str(expense.date)))
        self.connection.commit()

    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        rows = self.cursor.fetchall()
        expenses = []
        for row in rows:
            expense = Expense(row[1], row[2], row[3])
            expense.id = row[0]
            expense.date = row[4]
            expenses.append(expense)
        return expenses

    def delete_expense(self, expense_id):
        self.cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        self.connection.commit()
        return self.cursor.rowcount

    def close(self):
        self.connection.close()


