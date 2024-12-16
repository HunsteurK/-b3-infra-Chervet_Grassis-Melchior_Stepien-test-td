import unittest
from product import Product
from cart import Cart
from order import Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        # Setup products, cart, and order for testing
        self.product1 = Product(name="Laptop", price=1200.0, stock=5)
        self.product2 = Product(name="Mouse", price=25.0, stock=10)
        self.cart = Cart()
        print("\n[Setup] Created Cart and Product instances for testing.")

    def test_order_initialization_success(self):
        print("[Test] Testing Order Initialization (Success Case)...")
        self.cart.add_product(self.product1, 1)
        order = Order(self.cart)
        self.assertEqual(order.total, 1200.0)
        self.assertEqual(order.status, "Pending")
        print("[Test] Order Initialization (Success Case) passed.")

    def test_order_initialization_failure(self):
        print("[Test] Testing Order Initialization (Failure Case)...")
        with self.assertRaises(ValueError) as context:
            Order(self.cart)  # Cart is empty
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "Cart is empty. Cannot place an order.")
        print("[Test] Order Initialization (Failure Case) passed.")

    def test_place_order(self):
        print("[Test] Testing Place Order...")
        self.cart.add_product(self.product1, 2)
        order = Order(self.cart)
        result = order.place_order()
        self.assertEqual(order.status, "Completed")
        self.assertEqual(self.product1.stock, 3)  # Stock reduced
        self.assertIn("Order placed successfully", result)
        print("[Test] Place Order passed.")

    def test_cancel_order_success(self):
        print("[Test] Testing Cancel Order (Success Case)...")
        self.cart.add_product(self.product1, 1)
        order = Order(self.cart)
        result = order.cancel_order()
        self.assertEqual(order.status, "Canceled")
        self.assertEqual(result, "Order has been canceled.")
        print("[Test] Cancel Order (Success Case) passed.")

    def test_cancel_order_failure(self):
        print("[Test] Testing Cancel Order (Failure Case)...")
        self.cart.add_product(self.product1, 1)
        order = Order(self.cart)
        order.place_order()
        with self.assertRaises(ValueError) as context:
            order.cancel_order()  # Cannot cancel a completed order
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "Order cannot be canceled once it is completed.")
        print("[Test] Cancel Order (Failure Case) passed.")

    def test_add_tracking_success(self):
        print("[Test] Testing Add Tracking (Success Case)...")
        self.cart.add_product(self.product1, 1)
        order = Order(self.cart)
        order.place_order()
        result = order.add_tracking("TRACK123456")
        self.assertEqual(order.tracking_number, "TRACK123456")
        self.assertIn("Tracking number TRACK123456 has been added", result)
        print("[Test] Add Tracking (Success Case) passed.")

    def test_add_tracking_failure(self):
        print("[Test] Testing Add Tracking (Failure Case)...")
        self.cart.add_product(self.product1, 1)
        order = Order(self.cart)
        with self.assertRaises(ValueError) as context:
            order.add_tracking("TRACK123456")  # Cannot add tracking to pending order
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "Cannot add tracking to an order that is not completed.")
        print("[Test] Add Tracking (Failure Case) passed.")

    def test_update_order_status(self):
        print("[Test] Testing Update Order Status...")
        self.cart.add_product(self.product1, 1)
        order = Order(self.cart)
        result = order.update_order_status("Processing")
        self.assertEqual(order.status, "Processing")
        self.assertIn("Order status has been updated", result)
        print("[Test] Update Order Status passed.")

    def test_update_order_status_invalid(self):
        print("[Test] Testing Update Order Status (Invalid Case)...")
        self.cart.add_product(self.product1, 1)
        order = Order(self.cart)
        with self.assertRaises(ValueError) as context:
            order.update_order_status("Shipped")  # Invalid status
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "Invalid status. Valid statuses are: Pending, Processing, Completed, Canceled.")
        print("[Test] Update Order Status (Invalid Case) passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)
