from product import Product

class Cart:
    def __init__(self):
        self.items = {}  # {product: quantity}
        self.discount = 0  # Discount in percentage

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Cannot add {quantity} of {product.name}. Only {product.stock} left.")
        self.items[product] = self.items.get(product, 0) + quantity

    def remove_product(self, product: Product):
        if product in self.items:
            del self.items[product]
        else:
            raise KeyError(f"{product.name} is not in the cart.")

    def update_quantity(self, product: Product, quantity: int):
        if product not in self.items:
            raise KeyError(f"{product.name} is not in the cart.")
        if product.stock < quantity:
            raise ValueError(f"Cannot update to {quantity} of {product.name}. Only {product.stock} left.")
        if quantity == 0:
            self.remove_product(product)
        else:
            self.items[product] = quantity

    def clear_cart(self):
        self.items.clear()

    def apply_discount(self, discount_code: str):
        # Example: Define some predefined discount codes
        discounts = {
            "SAVE10": 10,
            "SAVE20": 20,
            "BLACKFRIDAY": 50
        }
        if discount_code in discounts:
            self.discount = discounts[discount_code]
        else:
            raise ValueError("Invalid discount code.")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items.items())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return total

    def display_cart(self):
        if not self.items:
            return "Your cart is empty."
        cart_content = "\n".join([f"{product.name} x {quantity} - {product.price * quantity}€"
                                     for product, quantity in self.items.items()])
        total = self.calculate_total()
        discount_info = f" (after {self.discount}% discount)" if self.discount > 0 else ""
        return f"{cart_content}\nTotal: {total:.2f}€{discount_info}"

