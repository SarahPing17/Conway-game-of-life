# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from cell import Cell
from board import Board
import json

with open('init.json') as f:
    data = json.load(f)

init_position = []

for position in data['init_pos']:
    init_position.append(position['position'])

print(init_position)

if __name__ == '__main__':

    rows = data['init_rows']
    columns = data['init_columns']

    conway_game_life = Board(rows,columns,init_position)

    conway_game_life.draw_board()

    i = 0

    while i < 10:
        conway_game_life.update_board()
        conway_game_life.draw_board()
        i = i + 1



