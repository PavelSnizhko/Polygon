from unittest.mock import patch
from unittest import TestCase

import unittest

from polygon_p.model.point import Point





class TestPoint(TestCase):
    def setUp(self):
        self.point = Point(10, 40)

    def test_get_x(self):
        self.assertEqual(self.point.get_x(), 10)
        self.assertNotEqual(self.point.get_x(), 30)

    @patch("polygon_p.point.Point.set_x")
    def test_set_x(self, set_x):
        self.point.set_x(20)
        self.assertTrue(set_x.called)
        self.assertEqual(set_x.call_args[0][0], 20)

    def test_get_y(self):
        self.assertEqual(self.point.get_y(), 40)
        self.assertNotEqual(self.point.get_y(), 50)

    @patch("polygon_p.point.Point.set_y")
    def test_set_y(self, set_y):
        self.point.set_y(10)
        self.assertTrue(set_y.called)
        self.assertNotEqual(set_y.call_args[0][0], 20)



if __name__ == '__main__':
    unittest.main()

