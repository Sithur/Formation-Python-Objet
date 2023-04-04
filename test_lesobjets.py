import unittest
from lesobjets import Point


class TestPoint(unittest.TestCase):
    """
    Class de test du type point
    """

    def test_creation_instance_point_sans_parametre(self):
        instance = Point()
        self.assertEqual(instance.x, 0)
        self.assertEqual(instance.y, 0)


    def test_move_un_point(self):
        instance = Point()
        instance.move(10,10)
        self.assertEqual(instance.x, 10)
        self.assertEqual(instance.y, 10)