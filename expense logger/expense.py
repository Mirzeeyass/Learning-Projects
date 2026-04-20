from datetime import date

class Expense:
    def __init__(self, title, amount, category):
        self.id = None
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date.today()

    def __str__(self):
        return f"[{self.id}] {self.title} | ${self.amount:.2f} | {self.category} | {self.date}"


# This is OUTSIDE the class — no indentation
expense1 = Expense("Coffee", 4.50, "Food")
print(expense1)