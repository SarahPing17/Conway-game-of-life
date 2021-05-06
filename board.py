from cell import Cell
from random import randint

class Board:
    def __init__(self, rows, columns, init_pos):
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]
        self.generate_board(init_pos)

    def draw_board(self):
        print('\n'*10)
        print('print board')
        for row in self._grid:
            for column in row:
                print(column.get_print_character(), end=' ')
            print()

    def generate_board(self, init_pos):
        print(init_pos)
        for item in init_pos:
            self._grid[item[0]][item[1]].set_alive()

    def check_neighbour(self, check_row, check_column):
        valid_neighbours_list = []
        for row in range(-1, 2):
            for column in range(-1, 2):
                target_row = check_row + row
                target_column = check_column + column
                valid_neighbour = True
                if (target_row) == check_row and (target_column) == check_column:
                    valid_neighbour = False

                if (target_row) < 0 or (target_row) >= self._rows:
                    valid_neighbour = False

                if (target_column) < 0 or (target_column) >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    valid_neighbours_list.append(self._grid[target_row][target_column])
        return valid_neighbours_list

    def update_board(self):
        print('updating board')
        will_alive = []
        will_dead = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                alive_neighbours = []

                current_valid_neighbours = self.check_neighbour(row,column)
                for item in current_valid_neighbours:
                    if item.is_alive():
                        alive_neighbours.append(item)

                if self._grid[row][column].is_alive() != True:
                    if len(alive_neighbours) == 3:
                        will_alive.append(self._grid[row][column])
                else:
                    if len(alive_neighbours) < 2 or len(alive_neighbours) > 3:
                        will_dead.append(self._grid[row][column])
                    if len(alive_neighbours) == 3 or len(alive_neighbours) == 2:
                        will_alive.append(self._grid[row][column])
        for item in will_alive:
            item.set_alive()
        for item in will_dead:
            item.set_dead()