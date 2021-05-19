import pygame, sys
from pygame.locals import *
import os
os.environ['PYGAME_FREETYPE'] = '1'
import pygame

import pygame as pg


class OutputMessage():
    def __init__(self, screen):
        self.screen = screen

    def displayTextAnimation(self, listOfMessage):

        message = listOfMessage[-1]
        myfont = pg.font.SysFont("Comic Sans MS", 17)
        yellow = (255, 255, 0)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        width = self.screen.get_width() // (10) * 8
        height = self.screen.get_height()
        width2 = self.screen.get_width() // (10) * 2
        xd = -30
        for i, xx in enumerate(listOfMessage):
            label = myfont.render(xx, 1, BLACK)
            xd = xd+30
            # print(height, " ")
            self.screen.blit(label, (width, xd, width2, height))
        # show the whole thing
        pg.display.flip()
        return "AAA"

    # def blit_text(self):
    #     BLACK = (0, 0, 0)
    #     font = pg.font.SysFont("Comic Sans MS", 17)
    #     words = [word.split(' ') for word in self.message.splitlines()]  # 2D array where each row is a list of words.
    #     space = font.size(' ')[0]  # The width of a space.
    #     max_width, max_height = self.screen.get_size()
    #     width = self.screen.get_width() // (10) * 8
    #     height = self.screen.get_height()
    #     width2 = self.screen.get_width() // (10) * 2
    #     x, y = width, height
    #     for line in words:
    #         for word in line:
    #             word_surface = font.render(word, 0, BLACK)
    #             word_width, word_height = word_surface.get_size()
    #             if x + word_width >= max_width:
    #                 x = width2  # Reset the x.
    #                 y += word_height  # Start on new row.
    #             self.screen.blit(word_surface, (width, 0, x, y))
    #             x += word_width + space
    #         x = width  # Reset the x.
    #         y += word_height  # Start on new row.
    #         pygame.display.update()
