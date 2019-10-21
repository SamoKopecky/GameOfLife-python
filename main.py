from Cell import *
from MainGui import *
import re
import sys
import os


def coords_from_file(file_name="coords.txt"):
    regex = lambda x: re.match(r'(\d+),(\d+)', x)
    file = open(file_name, 'r')
    coords = list(filter(regex, file.readlines()))
    coords = create_cell_from_coords(coords)
    file.close()
    return coords


def create_cell_from_coords(coords):
    created_cells = []
    for row in coords:
        middle_index = row.index(',')
        first_num = int(row[0:middle_index])
        second_num = int(row[middle_index + 1:])
        created_cells.append(Cell(first_num, second_num))
    return created_cells


def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()


def print_cells(positions):
    main_gui.reset_screen()
    main_gui.draw_grid()
    for cell in positions:
        main_gui.fill_on_position(cell.x, cell.y)


def init_all_cells(alive_cells):
    all_cells = alive_cells.copy()
    for cell in alive_cells:
        all_cells.extend(cell.init_alive_cell(all_cells, alive_cells))
    return all_cells


def init_game():
    positions = coords_from_file()
    print_cells(positions)
    return positions


def start_game(positions):
    while True:
        input()
        positions = init_all_cells(positions)
        positions = list(filter(Cell.apply_rules, positions))
        print_cells(positions)


main_gui = MainGui()
cells = init_game()
start_game(cells)
