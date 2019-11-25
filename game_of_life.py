# -*-coding:Utf-8 -*

from board import Board
from time import sleep

print("Welcome to the Game of Life !")
width = int(input("Choose the width of the board (70 recommended) : "))
height = int(input("Choose the height of the board (30 recommended): "))
board = Board(width, height)
day = 1
while True:
    print("Day " + str(day))
    day += 1
    board.render()
    board.next_state()
    sleep(0.075)
