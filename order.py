from cart import Cart

class Order:
    def __init__(self, cart: Cart):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot place an order.")
        self.items = cart.items
        self.total = cart.calculate_total()
        self.status = "Pending"  # New feature: Status tracking

    def place_order(self):
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)
        self.status = "Completed"  # Update status after successful order
        return f"Order placed successfully! Total: {self.total:.2f}€"

    def view_order(self):
        return "\n".join([f"{product.name} x {quantity}" for product, quantity in self.items.items()]) + \
               f"\nTotal: {self.total:.2f}€\nStatus: {self.status}"

    def cancel_order(self):
        if self.status != "Pending":
            raise ValueError("Order cannot be canceled once it is completed.")
        self.status = "Canceled"  # New feature: Cancel the order
        return "Order has been canceled."

    def add_tracking(self, tracking_number: str):
        if self.status != "Completed":
            raise ValueError("Cannot add tracking to an order that is not completed.")
        self.tracking_number = tracking_number  # New feature: Add tracking information
        return f"Tracking number {tracking_number} has been added to your order."

    def update_order_status(self, new_status: str):
        valid_statuses = ["Pending", "Processing", "Completed", "Canceled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}.")
        self.status = new_status  # New feature: Manually update order status
        return f"Order status has been updated to {new_status}."
