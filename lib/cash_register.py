class CashRegister:
    def __init__(self, discount=0):
        # Initializing discount, total, and items.
        self.discount = discount
        self.total = 0
        self.items = []  # Store items as dictionaries with 'title', 'price', and 'quantity'
        if not isinstance(discount, (int, float)):
            print("Discount should be a number.")
        else:
            self.discount = discount

    def add_item(self, title, price, quantity=1):
        if isinstance(title, str) and isinstance(price, (int, float)) and isinstance(quantity, int):
            # Store the item details (title, price, quantity) in the items list
            self.items.append({'title': title, 'price': price, 'quantity': quantity})
            self.total += price * quantity
        else:
            print("Invalid input for adding item.")

    def apply_discount(self):
        # Apply discount if it exists
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Void the last item added to the register
        if self.items:
            last_item = self.items[-1]  # Get the last item (a dictionary with 'title', 'price', 'quantity')
            self.items.remove(last_item)  # Remove the last item from items list
            # Subtract the price of the last item from the total
            self.total -= last_item['price'] * last_item['quantity']
        else:
            print("No items to void.")
