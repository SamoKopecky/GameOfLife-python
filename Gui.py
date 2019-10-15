import pygame


class Gui:
    def __init__(self):
        pygame.init()
        self.WHITE_COLOR = (250, 250, 250)
        self.RED_COLOR = (250, 0, 0)
        self.SIZES = {'width': 501,
                      'height': 501,
                      'cell': 20}  # 19 pixels sized cells
        self.screen = pygame.display.set_mode((self.SIZES['width'], self.SIZES['height']))

    def draw_grid(self):
        for i in range(int(self.SIZES['height'] / self.SIZES['cell']) + 1):
            top_offset = i * self.SIZES['cell']
            pygame.draw.line(self.screen, self.WHITE_COLOR, (0, top_offset), (self.SIZES['width'], top_offset))
        for i in range(int(self.SIZES['width'] / self.SIZES['cell']) + 1):
            left_offset = i * self.SIZES['cell']
            pygame.draw.line(self.screen, self.WHITE_COLOR, (left_offset, 0), (left_offset, self.SIZES['height']))
        pygame.display.flip()

    def fill_on_position(self, x, y):
        gui_start_x = x * self.SIZES['cell'] + 1
        gui_start_y = y * self.SIZES['cell'] + 1
        square = pygame.Rect(gui_start_x, gui_start_y, self.SIZES['cell'] - 1, self.SIZES['cell'] - 1)
        pygame.draw.rect(self.screen, self.RED_COLOR, square)
        pygame.display.update(square)

    def reset_screen(self):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, self.SIZES['width'], self.SIZES['height']))
