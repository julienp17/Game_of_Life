# -*-coding:Utf-8 -*
from __future__ import print_function
from random import randint
from colorama import Fore, Back, Style

class Board:

    """This class represents the board of the Game of Life."""

    def __init__(self, width, height):

        """Initialize the board with random cells."""

        self.width = width
        self.height = height
        self.state = self.get_random_state()

    def get_random_state(self):

        """Return a board state in which every cell has been randomly initialized
        to either ALIVE (represented by a 1) or DEAD (represented by a 0).

        This method is called when the board is created.

        """

        board = []

        for row in range(self.height):
            row = []
            for i in range(self.width):
                cell = randint(0, 1)
                row.append(cell)
            board.append(row)

        return board

    def next_state(self):

        """Change the board to the next state, according to the rules of
        the game of Life."""

        next_state = []

        for row in range(self.height):
            next_row = []
            for column in range(self.width):
                live_cells = 0
                cell = self.state[row][column]

                # 1ere ligne et colonne
                if (row - 1) < 0 and (column - 1) < 0:
                    try:
                        if self.state[row][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                # 1ere ligne
                elif (row - 1) < 0:
                    try:
                        if self.state[row][column - 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column - 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                # 1ere colonne
                elif (column - 1) < 0:
                    try:
                        if self.state[row - 1][column] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row - 1][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                else:
                    try:
                        if self.state[row - 1][column - 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row - 1][column] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row - 1][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row][column - 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column - 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                    try:
                        if self.state[row + 1][column + 1] == 1:
                            live_cells += 1
                    except IndexError:
                        pass
                if live_cells < 2:
                    cell = 0
                elif (live_cells == 2 or live_cells == 3) and cell == 1:
                    cell = 1
                elif live_cells == 3 and cell == 0:
                    cell = 1
                else:
                    cell = 0
                next_row.append(cell)
            next_state.append(next_row)

        self.state = next_state

    def render(self):

        """Format the board state and pretty print it to the terminal."""

        print("-" * ((self.width * 2) + 3))
        for row in range(self.height):
            print("| ", end = "")
            for column in range(self.width):
                if self.state[row][column] == 0:
                    print(Back.WHITE + " ", end = "")
                else:
                    print(Back.BLACK + " ", end = "")
                print(" " + Style.RESET_ALL, end = "")
            print("|")
        print("-" * ((self.width * 2) + 3))
