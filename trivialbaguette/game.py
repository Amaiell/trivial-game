import pygame as pg
from pawn import Pawn
# class to represent the game
class Game:

    def __init__(self):
        # generate a pawn
        """
        Get a reference to the screen (created in main); define necessary
        attributes; and create our player (draggable rect).
        """
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed()
        self.pawn = Pawn(self.screen_rect.center)
        #self.pawn = Pawn()
