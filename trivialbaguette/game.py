import pygame as pg
from pawn import Pawn
from part import Part
# class to represent the game
class Game:

    def __init__(self,player_number):
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
        self.player_number = player_number
        #for i in player
        self.pawn1 = Pawn(self.screen_rect.center,1)
        self.pawn2 = Pawn(self.screen_rect.center,2)
        self.pawn3 = Pawn(self.screen_rect.center,3)
        #self.pawn = Pawn()
        #camembert 1
        self.partblue_1 = Part(self.screen_rect.center,'blue',1)
        self.partyellow_1 = Part(self.screen_rect.center,'yellow',1)
        self.partpurple_1 = Part(self.screen_rect.center,'purple',1)
        self.partpink_1 = Part(self.screen_rect.center,'pink',1)
        self.partorange_1 = Part(self.screen_rect.center,'orange',1)
        self.partgreen_1 = Part(self.screen_rect.center,'green',1)
        #camembert 2
        self.partblue_2 = Part(self.screen_rect.center,'blue',2)
        self.partyellow_2 = Part(self.screen_rect.center,'yellow',2)
        self.partpurple_2 = Part(self.screen_rect.center,'purple',2)
        self.partpink_2 = Part(self.screen_rect.center,'pink',2)
        self.partorange_2 = Part(self.screen_rect.center,'orange',2)
        self.partgreen_2 = Part(self.screen_rect.center,'green',2)
        #camembert 3
        self.partblue_3 = Part(self.screen_rect.center,'blue',3)
        self.partyellow_3 = Part(self.screen_rect.center,'yellow',3)
        self.partpurple_3 = Part(self.screen_rect.center,'purple',3)
        self.partpink_3 = Part(self.screen_rect.center,'pink',3)
        self.partorange_3 = Part(self.screen_rect.center,'orange',3)
        self.partgreen_3 = Part(self.screen_rect.center,'green',3)
