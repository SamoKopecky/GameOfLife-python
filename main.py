from Cell import *
import re
import sys
import os
import random


def clear_screen():
    os.system('clear')


def print_there(x, y, text):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
    sys.stdout.flush()


def create_first_list():
    print("Enter positions:")
    pattern = r'(\d+),(\d+)'
    cords = []
    while True:
        input_cords = input()
        if not re.match(pattern, input_cords):
            return cords

        middle_index = input_cords.index(',')
        first_num = int(input_cords[0:middle_index])
        second_num = int(input_cords[middle_index + 1:])
        cords.append(Cell(first_num, second_num, True))


def print_cells(positions):
    clear_screen()
    for cell in positions:
        if cell.alive:
            print_there(cell.x + 15, cell.y + 15, "*")
        else:
            print_there(cell.x + 15, cell.y + 15, "-")


def init_all_cells(alive_cells):
    all_cells = alive_cells.copy()
    for cell in alive_cells:
        all_cells.extend(cell.init_alive_cell(all_cells, alive_cells))
    return all_cells


def init_game():
    # positions = create_first_list()
    cells = [Cell(1, 1, True), Cell(2, 2, True), Cell(3, 1, True), Cell(3, 2, True), Cell(3, 0, True)]
    print_cells(cells)
    return cells


def start_game(cells):
    while True:
        input()
        cells = init_all_cells(cells)
        cells = list(filter(Cell.apply_rules, cells))
        print_cells(cells)


cells = init_game()
start_game(cells)
