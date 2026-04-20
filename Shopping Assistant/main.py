from database import Database
from shopping_item import ShoppingItem
from ai_helper import AIHelper

db = Database("shopping.db")
ai = AIHelper("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")

while True:
    print("\n--- Shopping List Assistant ---")
    print("1. Add item")
    print("2. View list")
    print("3. Mark as bought")
    print("4. Get AI suggestions")
    print("5. Delete item")
    print("6. Quit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        name = input("Item name: ")
        quantity = int(input("Quantity: "))
        category = input("Category: ")
        item = ShoppingItem(name, quantity, category)
        db.add_item(item)
        print("Item added!")

    elif choice == "2":
        items = db.get_all_items()
        if len(items) == 0:
            print("Your list is empty.")
        else:
            for item in items:
                print(item)

    elif choice == "3":
        item_id = int(input("Enter item id to mark as bought: "))
        updated = db.mark_as_bought(item_id)
        if updated:
            print("Marked as bought!")
        else:
            print("Item not found!")

    elif choice == "4":
        items = db.get_all_items()
        if len(items) == 0:
            print("Add some items first!")
        else:
            print("\nAsking AI for suggestions...")
            suggestions = ai.suggest_items(items)
            print("\nAI suggests you might also need:")
            print(suggestions)

    elif choice == "5":
        item_id = int(input("Enter item id to delete: "))
        deleted = db.delete_item(item_id)
        if deleted:
            print("Item deleted!")
        else:
            print("Item not found!")

    elif choice == "6":
        db.close()
        print("Goodbye!")
        break
    