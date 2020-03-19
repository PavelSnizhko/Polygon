import unittest
from unittest import TestCase
from unittest.mock import patch

from polygon.polygon import Polygon


class TestPolygon(TestCase):
    def setUp(self):
        self.polygon = Polygon(10, 20, 30, 50)
        self.polygon.set_a(20)

    def test_calculate_square(self):
        self.assertNotEqual(self.polygon.calculate_square(), 5456.366088464047)

    def test_get_n(self):
        self.assertEqual(self.polygon.get_n(), 30)
        self.assertNotEqual(self.polygon.get_n(), 40)

    @patch("polygon.polygon.Polygon.set_n")
    def test_set_n(self, set_n):
        self.polygon.set_n(20)
        self.assertTrue(set_n.called)
        self.assertEqual(set_n.call_args[0][0], 20)

    def test_get_a(self):
        self.assertNotEqual(self.polygon.get_n(), 60)
        self.assertNotEqual(self.polygon.get_n(), 40)

    @patch("polygon.polygon.Polygon.set_a")
    def test_set_a(self, set_a):
        self.polygon.set_a(40)
        self.assertTrue(set_a.called)
        self.assertEqual(set_a.call_args[0][0], 40)

if __name__ == '__main__':
    unittest.main()