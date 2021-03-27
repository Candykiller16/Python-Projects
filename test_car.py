import unittest
from task_14_test import Car
car_1 = Car('Tesal', 'modelX', 2012, 10)

class TestCarMethods(unittest.TestCase):
    def test_increase(self):
        self.assertEqual(car_1.increase(), 20)

    def test_reduce(self):
        self.assertEqual(car_1.reduce(), 5)

    def test_stop(self):
        self.assertEqual(car_1.stop(), 0)

    def test_show_speed(self):
        self.assertEqual(car_1.show_speed(), 10)

    def test_changes(self):
        self.assertEqual(car_1.changes(), -10)