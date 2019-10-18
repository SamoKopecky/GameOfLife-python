from Cell import *
from Gui import *
import sys
import os
import random


def cords_from_file(file_name="cords.txt"):
    coords = []
    file = open(file_name, "r")
    for line in file.readlines():
        coords.append(line)
    file.close()
    return coords


def clear_screen():
    os.system('clear')


def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()


def print_cells(positions):
    gui.reset_screen()
    gui.draw_grid()
    for cell in positions:
        gui.fill_on_position(cell.x, cell.y)


def init_all_cells(alive_cells):
    all_cells = alive_cells.copy()
    for cell in alive_cells:
        all_cells.extend(cell.init_alive_cell(all_cells, alive_cells))
    return all_cells


def init_game():
    positions = [Cell(1, 1), Cell(2, 2), Cell(3, 1), Cell(3, 2), Cell(3, 0),
                 Cell(6, 6), Cell(7, 7), Cell(8, 6), Cell(8, 7), Cell(8, 5)]
    print_cells(positions)
    return positions


def start_game(positions):
    while True:
        input()
        positions = init_all_cells(positions)
        positions = list(filter(Cell.apply_rules, positions))
        print_cells(positions)


gui = Gui()
gui.draw_grid()
cells = init_game()
start_game(cells)
