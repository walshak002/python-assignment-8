"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add(self, item, quantity=1):
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity
    def remove(self, item):
        if item in self.cart:
            del self.cart[item]
        else:
            f"{item} not fount in cart"
    def clear(self, item):
        self.cart.clear()

    def show_cart(self):
        if not self.cart:
            return "Cart is empty."
        return self.cart


    
cart = ShoppingCart()

cart.add("Apple", 1)
cart.add("Banana", 2)
cart.add("Orange", 3)
cart.add("Mango", 4)

cart.remove("Mango")

print(cart.show_cart())

price = {"shirt": 5000, "shoes": 120000}