import pygame
from ui.textbox import Textbox


class Renderer:
    def __init__(self, window, width, background_color, score_tracker):
        self._window = window
        self._width = width
        self._background_color = background_color
        self._score_tracker = score_tracker

    def redraw(self, x, y, symbol_image):
        self._window.fill(self._background_color)
        self._window.blit(symbol_image, (x, y))
        textbox = Textbox(self._window, self._width, self._score_tracker)
        textbox.add_text()
        pygame.display.update()
