import unittest
from unittest import TestCase

# from projects.lab.proxy import Proxy
# from projects.lab.proxy import Proxy
from polygon_p.model.proxy import Proxy


class TestProxy(TestCase):
    def setUp(self):
        self.proxy = Proxy(50, 30, 30, 50)

    def test_get_n(self):
        self.assertEqual(self.proxy.get_n(), 30)

    def test_get_a(self):
        self.assertEqual(self.proxy.get_a(), 50)
        self.assertNotEqual(self.proxy.get_a(), 10)

    def test_calculate_square(self):
        self.assertEqual(self.proxy.calculate_square(), 5456.366088464047)

    def test_set_n(self):
        with self.assertRaises(Exception) as context:
            self.proxy.set_n(50)

        self.assertTrue("You can't use a setter function" in str(context.exception))

    def test_set_a(self):
        with self.assertRaises(Exception) as context:
            self.proxy.set_a(30)

        self.assertTrue("You can't use a setter function" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
