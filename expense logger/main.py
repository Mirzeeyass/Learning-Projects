from database import Database
from expense import Expense

db = Database("expenses.db")

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Delete expense")
    print("4. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        title = input("Title: ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        expense = Expense(title, amount, category)
        db.add_expense(expense)
        print("Expense added!")

    elif choice == "2":
        expenses = db.get_all_expenses()
        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            for expense in expenses:
                print(expense)

    elif choice == "3":
        expense_id = int(input("Enter expense id to delete: "))
        deleted = db.delete_expense(expense_id)
        if deleted:
            print("Expense deleted!")
        else:
            print("Expense not found!")

    elif choice == "4":
        db.close()
        print("Goodbye!")
        break
