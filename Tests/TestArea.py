import unittest
from src.Area import Area
from src.Block import Colors

class TestArea(unittest.TestCase):
    def setUp(self):
        self.area = Area(size_x=5, size_y=5, id=1)

    def test_size_x(self):  
        self.assertEqual(self.area.get_size_x(), 5)

    def test_size_y(self):
        self.assertEqual(self.area.get_size_y(), 5)
    
    def test_center(self):
        self.assertEqual(self.area.get_center(), 1.0)

    def test_color(self):
        self.area.set_color(Colors.RED)
        self.assertEqual(self.area.get_color(), Colors.RED)
    
    def test_id(self):
        self.area.set_id(2)
        self.assertEqual(self.area.get_id(), 2)

if __name__ == '__main__':
    unittest.main()