import unittest
from product import Product
from cart import Cart

class TestCart(unittest.TestCase):

    def setUp(self):
        # Setup products and a cart instance for testing
        self.product1 = Product(name="Laptop", price=1200.0, stock=5)
        self.product2 = Product(name="Mouse", price=25.0, stock=50)
        self.cart = Cart()
        print("\n[Setup] Created Cart and Product instances for testing.")

    def test_add_product_success(self):
        print("[Test] Testing Add Product (Success Case)...")
        self.cart.add_product(self.product1, 2)
        self.assertIn(self.product1, self.cart.items)
        self.assertEqual(self.cart.items[self.product1], 2)
        print("[Test] Add Product (Success Case) passed.")

    def test_add_product_failure(self):
        print("[Test] Testing Add Product (Failure Case)...")
        with self.assertRaises(ValueError) as context:
            self.cart.add_product(self.product1, 10)  # Exceeds stock
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "Cannot add 10 of Laptop. Only 5 left.")
        print("[Test] Add Product (Failure Case) passed.")

    def test_remove_product_success(self):
        print("[Test] Testing Remove Product (Success Case)...")
        self.cart.add_product(self.product1, 1)
        self.cart.remove_product(self.product1)
        self.assertNotIn(self.product1, self.cart.items)
        print("[Test] Remove Product (Success Case) passed.")

    def test_remove_product_failure(self):
        print("[Test] Testing Remove Product (Failure Case)...")
        with self.assertRaises(KeyError) as context:
            self.cart.remove_product(self.product1)  # Product not in cart
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "'Laptop is not in the cart.'")
        print("[Test] Remove Product (Failure Case) passed.")

    def test_update_quantity_success(self):
        print("[Test] Testing Update Quantity (Success Case)...")
        self.cart.add_product(self.product1, 1)
        self.cart.update_quantity(self.product1, 3)
        self.assertEqual(self.cart.items[self.product1], 3)
        print("[Test] Update Quantity (Success Case) passed.")

    def test_update_quantity_failure(self):
        print("[Test] Testing Update Quantity (Failure Case)...")
        with self.assertRaises(KeyError) as context:
            self.cart.update_quantity(self.product1, 2)  # Product not in cart
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "'Laptop is not in the cart.'")
        print("[Test] Update Quantity (Failure Case) passed.")

    def test_clear_cart(self):
        print("[Test] Testing Clear Cart...")
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 2)
        self.cart.clear_cart()
        self.assertEqual(len(self.cart.items), 0)
        print("[Test] Clear Cart passed.")

    def test_apply_discount_success(self):
        print("[Test] Testing Apply Discount (Success Case)...")
        self.cart.add_product(self.product1, 1)
        self.cart.apply_discount("SAVE10")  # Apply 10% discount
        total = self.cart.calculate_total()
        self.assertAlmostEqual(total, 1080.0)  # 1200 - 10%
        print("[Test] Apply Discount (Success Case) passed.")

    def test_apply_discount_failure(self):
        print("[Test] Testing Apply Discount (Failure Case)...")
        with self.assertRaises(ValueError) as context:
            self.cart.apply_discount("INVALIDCODE")
        print(f"[Test] Caught exception: {context.exception}")
        self.assertEqual(str(context.exception), "Invalid discount code.")
        print("[Test] Apply Discount (Failure Case) passed.")

    def test_display_cart(self):
        print("[Test] Testing Display Cart...")
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 2)
        expected_output = (
            "Laptop x 1 - 1200.0\u20ac\n"
            "Mouse x 2 - 50.0\u20ac\n"
            "Total: 1250.00\u20ac"
        )
        self.assertEqual(self.cart.display_cart(), expected_output)
        print("[Test] Display Cart passed.")

if __name__ == "__main__":
    unittest.main(buffer=False)
