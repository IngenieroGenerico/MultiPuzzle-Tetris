import unittest
from Game import Grid, PieceType, Piece

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test_create_level(self):
        self.grid.create_level(areas_amount=3, size_x=10, size_y=20)
        self.assertEqual(self.grid.get_areas_amount(), 3)
        self.assertIsNotNone(self.grid.get_actual_piece())
        self.assertIsNotNone(self.grid.get_next_piece())
    
    def test_spawn_piece_in_area(self):
        pass

    def test_create_areas(self):
        self.grid.create_areas(amount=3, size_x=10, size_y=20)
        self.assertEqual(len(self.grid.__grid), 3)
    
    def test_create_piece(self):
        piece = self.grid.create_piece(piece=PieceType.I)
        self.assertIsInstance(piece, Piece)
    
    def test_switch(self):
        piece = self.grid.switch(PieceType.O)
        self.assertIsInstance(piece, Piece)

    def test_get_actual_piece(self):
        self.assertIsNone(self.grid.get_actual_piece())
    
    def test_get_next_piece(self):
        self.assertIsNone(self.grid.get_next_piece())

    def test_get_area_size_x(self):
        self.grid.create_areas(amount=3, size_x=10, size_y=20)
        self.assertEqual(self.grid.get_area_size_x(), 10)

    def test_get_area_size_x(self):
        self.grid.create_areas(amount=3, size_x=10, size_y=20)
        self.assertEqual(self.grid.get_area_size_y(), 20)

if __name__ == '__main__':
    unittest.main()