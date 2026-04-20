import sqlite3
from shopping_item import ShoppingItem


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                quantity INTEGER,
                category TEXT,
                bought INTEGER DEFAULT 0
            )
        """)
        self.connection.commit()

    def add_item(self, item):
        self.cursor.execute("""
            INSERT INTO items (name, quantity, category, bought)
            VALUES (?, ?, ?, ?)
        """, (item.name, item.quantity, item.category, 0))
        self.connection.commit()

    def get_all_items(self):
        self.cursor.execute("SELECT * FROM items")
        rows = self.cursor.fetchall()
        items = []
        for row in rows:
            item = ShoppingItem(row[1], row[2], row[3])
            item.id = row[0]
            item.bought = bool(row[4])
            items.append(item)
        return items

    def mark_as_bought(self, item_id):
        self.cursor.execute("UPDATE items SET bought = 1 WHERE id = ?", (item_id,))
        self.connection.commit()
        return self.cursor.rowcount

    def delete_item(self, item_id):
        self.cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
        self.connection.commit()
        return self.cursor.rowcount

    def close(self):
        self.connection.close()


# Test
db = Database("shopping.db")
item1 = ShoppingItem("Milk", 2, "Dairy")
item2 = ShoppingItem("Eggs", 12, "Dairy")
db.add_item(item1)
db.add_item(item2)

all_items = db.get_all_items()
for item in all_items:
    print(item)

db.close()

