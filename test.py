# -*-coding:Utf-8 -*

from unittest import TestCase
from board import Board

class TestGameOfLife(TestCase):

    """This class test the features of the Game of Life."""

    def setUp(self):

        """Create a 3x3 board object."""

        self.board = Board(3, 3)

    def test_rule1(self):

        """RULE 1 : Any live cell with 0 or 1 live neighbors becomes dead,
        because of underpopulation."""

        init_state = [
            [1, 0, 1], # First : 1, Second : 3, Third : 0
            [1, 0, 0], # First : 1, Second : 4, Third : 2
            [0, 0, 1]  # First : 1, Second : 2, Third : 0
        ]

        expected_next_state = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.board.state = init_state
        self.board.next_state()

        actual_next_state = self.board.state

        self.assertEqual(expected_next_state, actual_next_state)

    def test_rule2(self):

        """RULE 2 : Any live cell with 2 or 3 live neighbors stays alive,
        because its neighborhood is just right"""

        init_state = [
            [1, 0, 0], # First : 2, Second : 3, Third : 1
            [1, 1, 0], # First : 3, Second : 3, Third : 1
            [1, 0, 0]  # First : 2, Second : 3, Third : 1
        ]

        expected_next_state = [
            [1, 1, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]

        self.board.state = init_state
        self.board.next_state()

        actual_next_state = self.board.state

        self.assertEqual(expected_next_state, actual_next_state)

    def test_rule3(self):

        """RULE 3 : Any live cell with more than 3 live neighbors becomes dead,
        because of overpopulation"""

        init_state = [
            [1, 1, 0], # First : 3, Second : 3, Third : 2
            [1, 1, 0], # First : 5, Second : 5, Third : 3
            [1, 1, 0]  # First : 3, Second : 3, Third : 2
        ]

        expected_next_state = [
            [1, 1, 0],
            [0, 0, 1],
            [1, 1, 0]
        ]

        self.board.state = init_state
        self.board.next_state()

        actual_next_state = self.board.state

        self.assertEqual(expected_next_state, actual_next_state)

    def test_rule4(self):

        """RULE 4 : Any dead cell with exactly 3 live neighbors becomes alive, 
        by reproduction."""

        init_state = [
            [0, 0, 1], # First : 1, Second : 3, Third : 2
            [0, 1, 1], # First : 1, Second : 2, Third : 2
            [0, 0, 0]  # First : 1, Second : 2, Third : 2
        ]

        expected_next_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]

        self.board.state = init_state
        self.board.next_state()

        actual_next_state = self.board.state

        self.assertEqual(expected_next_state, actual_next_state)

    def test_all_dead(self):

        """TEST ALL DEAD: dead cells with no live neighbors should stay dead."""

        init_state = [
            [0, 0, 0], # First : 0, Second : 0, Third : 0
            [0, 0, 0], # First : 0, Second : 0, Third : 0
            [0, 0, 0]  # First : 0, Second : 0, Third : 0
        ]

        expected_next_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.board.state = init_state
        self.board.next_state()

        actual_next_state = self.board.state

        self.assertEqual(expected_next_state, actual_next_state)

    def test_all_alive(self):

        """TEST ALL ALIVE: a board full of live cells should stay alive on its sides."""

        init_state = [
            [1, 1, 1], # First : 3, Second : 5, Third : 3
            [1, 1, 1], # First : 5, Second : 8, Third : 5
            [1, 1, 1]  # First : 3, Second : 5, Third : 3
        ]

        expected_next_state = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]

        self.board.state = init_state
        self.board.next_state()

        actual_next_state = self.board.state

        self.assertEqual(expected_next_state, actual_next_state)

if __name__ == '__main__':
    unittest.main()
