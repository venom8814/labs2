import unittest
from order_calculator import calculate_order

class TestCalculateOrder(unittest.TestCase):

    def test_tc01_standard_no_discount(self):
        self.assertEqual(calculate_order(1000, 2, 0, "standard"), 2300.0)

    def test_tc02_standard_discount_10(self):
        self.assertEqual(calculate_order(1000, 5, 10, "standard"), 4800.0)

    def test_tc03_express_no_discount(self):
        self.assertEqual(calculate_order(500, 3, 0, "express"), 2100.0)

    def test_tc04_free_delivery_over_10000(self):
        self.assertEqual(calculate_order(6000, 2, 0, "express"), 12000.0)

    def test_tc05_boundary_price_zero(self):
        self.assertEqual(calculate_order(0, 10, 0, "standard"), 300.0)

    def test_tc06_boundary_quantity_zero(self):
        self.assertEqual(calculate_order(1000, 0, 0, "standard"), 300.0)

    def test_tc07_boundary_discount_100(self):
        self.assertEqual(calculate_order(500, 1, 100, "standard"), 300.0)

    def test_tc08_boundary_cost_exactly_10000(self):
        self.assertEqual(calculate_order(1000, 10, 0, "standard"), 10300.0)

    def test_tc09_error_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order(-100, 5, 10, "standard")

    def test_tc10_error_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, -1, 0, "standard")

    def test_tc11_error_discount_above_100(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, 1, 150, "standard")

    def test_tc12_error_discount_negative(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, 1, -10, "standard")

    def test_tc13_error_unknown_delivery(self):
        with self.assertRaises(ValueError):
            calculate_order(1000, 1, 0, "fast")

    def test_tc14_express_discount_free_delivery(self):
        self.assertEqual(calculate_order(2000, 6, 10, "express"), 10800.0)

    def test_tc15_minimal_order_standard(self):
        self.assertEqual(calculate_order(1, 1, 0, "standard"), 301.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
