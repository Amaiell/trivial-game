#project of trivial pursuit game : virtual version
import os
import pygame as pg
from game import Game
from PIL import Image
pg.init()

        
#generate the game window
icon = pg.image.load('assets/images/icon-baguette.jpg')
pg.display.set_icon(icon)
pg.display.set_caption("Poursuite Banale : Baguette edition")
screen = pg.display.set_mode((1080,700))

#width = GetSystemMetrics (0)
#height = GetSystemMetrics (1)
#pygame.display.set_mode((width,height),FULLSCREEN)

#upload background of the game
background = pg.image.load('assets/images/board.png')
background = pg.transform.scale(background, (800,720))

#charge the game
game = Game()

running = True

#loop running (keping the window open)
while running:

    #apply the background
    screen.blit(background, (140,0))

    #apply the image of the pawn

    screen.blit(game.pawn.image, game.pawn.rect)

    #update background
    pg.display.flip()

    #If the player closes the window
    for event in pg.event.get():
        #check if the event is closing the window
        if event.type == pg.QUIT or game.keys[pg.K_ESCAPE]:
            running = False
            pg.quit()
            print("Closing the game")
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                game.pawn.check_click(event.pos)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                game.pawn.click = False
        elif event.type in (pg.KEYUP, pg.KEYDOWN):
                game.keys = pg.key.get_pressed() 

