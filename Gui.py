import pygame


class Gui:
    def __init__(self):
        pygame.init()
        self.WHITE = (250, 250, 250)
        self.RED = (250, 0, 0)
        self.BLACK = (0, 0, 0)
        self.CELL_SIZE = 19
        self.LINE_SIZE = 1
        self.CELLS_WIDE = 35
        self.CELLS_HIGH = 20
        self.LINES_WIDE = self.CELLS_WIDE + self.LINE_SIZE
        self.LINES_HIGH = self.CELLS_HIGH + self.LINE_SIZE
        self.WIDTH = self.LINES_WIDE + self.CELLS_WIDE * self.CELL_SIZE
        self.HEIGHT = self.LINES_HIGH + self.CELLS_HIGH * self.CELL_SIZE
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def draw_grid(self):
        for offset in self.get_offset(self.LINES_HIGH):
            pygame.draw.line(self.screen, self.WHITE, (0, offset), (self.WIDTH, offset))
        for offset in self.get_offset(self.LINES_WIDE):
            pygame.draw.line(self.screen, self.WHITE, (offset, 0), (offset, self.HEIGHT))
        pygame.display.flip()

    def get_offset(self, size):
        for i in range(size):
            yield i * (self.CELL_SIZE + self.LINE_SIZE)

    def fill_on_position(self, x, y):
        start = lambda a: a * (self.CELL_SIZE + self.LINE_SIZE) + self.LINE_SIZE
        start_x = start(x)
        start_y = start(y)
        square = pygame.Rect(start_x, start_y, self.CELL_SIZE, self.CELL_SIZE)
        pygame.draw.rect(self.screen, self.RED, square)
        pygame.display.update(square)

    def reset_screen(self):
        pygame.draw.rect(self.screen, self.BLACK, pygame.Rect(0, 0, self.WIDTH, self.HEIGHT))
