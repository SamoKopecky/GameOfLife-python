class Cell:
    def __init__(self, x, y, alive=True):
        self.x = x
        self.y = y
        self.alive = alive
        self.neighbours = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "x is : {} and y is : {} and neighbours are : {}".format(self.x, self.y, self.neighbours)

    def init_alive_cell(self, all_cells, alive_cells):
        surroundings = []
        for cell in self.create_neighbours():
            if cell in alive_cells:
                cell.alive = True
                self.neighbours = self.neighbours + 1
                continue
            elif cell in all_cells:
                continue
            else:
                cell.init_dead_cell(alive_cells)
                surroundings.append(cell)
        return surroundings

    def init_dead_cell(self, alive_positions):
        for cell in self.create_neighbours():
            if cell in alive_positions:
                self.neighbours += 1

    def create_neighbours(self):
        lambdas = [lambda x, y: Cell(x - 1, y - 1, False),
                   lambda x, y: Cell(x - 1, y, False),
                   lambda x, y: Cell(x - 1, y + 1, False),
                   lambda x, y: Cell(x, y - 1, False),
                   lambda x, y: Cell(x, y + 1, False),
                   lambda x, y: Cell(x + 1, y - 1, False),
                   lambda x, y: Cell(x + 1, y, False),
                   lambda x, y: Cell(x + 1, y + 1, False)]
        for move in lambdas:
            yield move(self.x, self.y)

    @staticmethod
    def apply_rules(cell):
        if cell.alive is True:
            cell.alive = True
            return 2 <= cell.get_neighbours() <= 3
        else:
            cell.alive = True
            return cell.get_neighbours() == 3

    def get_neighbours(self):
        neighbours = self.neighbours
        self.neighbours = 0
        return neighbours
