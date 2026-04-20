class ShoppingItem:
    def __init__(self, name, quantity, category):
        self.id = None
        self.name = name
        self.quantity = quantity
        self.category = category
        self.bought = False

    def __str__(self):
        status = "✓" if self.bought else "✗"
        return f"[{self.id}] {status} {self.name} | Qty: {self.quantity} | {self.category}"


# Test
item1 = ShoppingItem("Milk", 2, "Dairy")
print(item1)