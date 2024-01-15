import unittest
from src.Block import Block, Color

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(x=1, y=2, color=Color.RED)

    def test_set_and_get_color(self):
        self.block.set_color(Color.BLUE)
        self.assertEqual(self.block.get_color(), Color.BLUE)

    def test_get_color_rgb(self):
        self.assertEqual(self.block.get_color_rgb(), (255, 0, 0))

    def test_set_and_get_position(self):
        self.block.set_position(3, 4)
        self.assertEqual(self.block.get_position(), (3, 4))

    def test_move_down(self):
        pos_y = self.block.get_position()[1]
        self.block.move_down()
        self.assertEqual(self.block.get_position()[1], pos_y - 1)
    
    def test_move_left(self):
        pos_x = self.block.get_position()[0]
        self.block.move_left()
        self.assertEqual(self.block.get_position()[0], pos_x - 1)

    def test_move_right(self):
        pos_x = self.block.get_position()[0]
        self.block.move_right()
        self.assertEqual(self.block.get_position()[0], pos_x + 1)
    
    def test_get_rect(self):
        self.block.create_rect(0, 0)
        self.assertIsNotNone(self.block.get_rect())

if __name__ == '__main__':
    unittest.main()