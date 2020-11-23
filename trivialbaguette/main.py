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
background = pg.image.load('assets/images/background.png')
board = pg.image.load('assets/images/board.png')
board = pg.transform.scale(board, (750,720))
camembert = pg.image.load('assets/images/camembert.png')
camembert = pg.transform.scale(camembert, (150,150))
#charge the game
game = Game(3)

running = True

#loop running (keping the window open)
while running:

    #apply the background
    screen.blit(background, (0,0))
    screen.blit(board, (0,0))
    screen.blit(camembert, (900,40))
    screen.blit(camembert, (900,190))
    screen.blit(camembert, (900,340))

    #display text
    font = pg.font.SysFont('Calibri', 30)
    screen.blit(font.render('Team 1', True,pg.Color("white")), (800, 100))
    screen.blit(font.render('Team 2', True,pg.Color("white")), (800, 250))
    screen.blit(font.render('Team 3', True,pg.Color("white")), (800, 400))

    #apply the image of the pawn
    screen.blit(game.pawn1.image, game.pawn1.rect)
    screen.blit(game.pawn2.image, game.pawn2.rect)
    screen.blit(game.pawn3.image, game.pawn3.rect)
    
    #apply the image of the camemberts first team
    screen.blit(game.partblue_1.image, game.partblue_1.rect)
    screen.blit(game.partyellow_1.image, game.partyellow_1.rect)
    screen.blit(game.partpurple_1.image, game.partpurple_1.rect)
    screen.blit(game.partpink_1.image, game.partpink_1.rect)
    screen.blit(game.partorange_1.image, game.partorange_1.rect)
    screen.blit(game.partgreen_1.image, game.partgreen_1.rect)

    #apply the image of the camemberts first team
    screen.blit(game.partblue_2.image, game.partblue_2.rect)
    screen.blit(game.partyellow_2.image, game.partyellow_2.rect)
    screen.blit(game.partpurple_2.image, game.partpurple_2.rect)
    screen.blit(game.partpink_2.image, game.partpink_2.rect)
    screen.blit(game.partorange_2.image, game.partorange_2.rect)
    screen.blit(game.partgreen_2.image, game.partgreen_2.rect)
    

    #apply the image of the camemberts first team
    screen.blit(game.partblue_3.image, game.partblue_3.rect)
    screen.blit(game.partyellow_3.image, game.partyellow_3.rect)
    screen.blit(game.partpurple_3.image, game.partpurple_3.rect)
    screen.blit(game.partpink_3.image, game.partpink_3.rect)
    screen.blit(game.partorange_3.image, game.partorange_3.rect)
    screen.blit(game.partgreen_3.image, game.partgreen_3.rect)
    

    #update background
    pg.display.flip()

    #If the player closes the window
    for event in pg.event.get():
        #check if the event is closing the window
        if event.type == pg.QUIT : #or game.keys[pg.K_ESCAPE]:
            running = False
            pg.quit()
            print("Closing the game")
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE :
                running = False
                pg.quit()
                print("Closing the game")
                #pawn 1
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                game.pawn1.check_click(event.pos)
                game.pawn2.check_click(event.pos)
                game.pawn3.check_click(event.pos)
                #check if clicking on camembert 1
                game.partblue_1.check_click(event.pos)
                game.partyellow_1.check_click(event.pos)
                game.partpurple_1.check_click(event.pos)
                game.partpink_1.check_click(event.pos)
                game.partorange_1.check_click(event.pos)
                game.partgreen_1.check_click(event.pos)
                #cheking if clicking on camebert 2
                game.partblue_2.check_click(event.pos)
                game.partyellow_2.check_click(event.pos)
                game.partpurple_2.check_click(event.pos)
                game.partpink_2.check_click(event.pos)
                game.partorange_2.check_click(event.pos)
                game.partgreen_2.check_click(event.pos)
                #cheking if clicking on camebert 3
                game.partblue_3.check_click(event.pos)
                game.partyellow_3.check_click(event.pos)
                game.partpurple_3.check_click(event.pos)
                game.partpink_3.check_click(event.pos)
                game.partorange_3.check_click(event.pos)
                game.partgreen_3.check_click(event.pos)
                print("appuie plus fort !")
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                game.pawn1.click = False
                game.pawn2.click = False
                game.pawn3.click = False

                #changing statues on camembert 1
                game.partblue_1.click = False
                screen.blit(game.partblue_1.image, game.partblue_1.rect)
                game.partyellow_1.click = False
                screen.blit(game.partyellow_1.image, game.partyellow_1.rect)
                game.partpurple_1.click = False
                screen.blit(game.partpurple_1.image, game.partpurple_1.rect)
                game.partpink_1.click = False
                screen.blit(game.partpink_1.image, game.partpink_1.rect)
                game.partorange_1.click = False
                screen.blit(game.partorange_1.image, game.partorange_1.rect)
                game.partgreen_1.click = False
                screen.blit(game.partgreen_1.image, game.partgreen_1.rect)

                #changing statues on camembert 2
                game.partblue_2.click = False
                screen.blit(game.partblue_2.image, game.partblue_2.rect)
                game.partyellow_2.click = False
                screen.blit(game.partyellow_2.image, game.partyellow_2.rect)
                game.partpurple_2.click = False
                screen.blit(game.partpurple_2.image, game.partpurple_2.rect)
                game.partpink_2.click = False
                screen.blit(game.partpink_2.image, game.partpink_2.rect)
                game.partorange_2.click = False
                screen.blit(game.partorange_2.image, game.partorange_2.rect)
                game.partgreen_2.click = False
                screen.blit(game.partgreen_2.image, game.partgreen_2.rect)

                #changing statues on camembert 3
                game.partblue_3.click = False
                screen.blit(game.partblue_3.image, game.partblue_3.rect)
                game.partyellow_3.click = False
                screen.blit(game.partyellow_3.image, game.partyellow_3.rect)
                game.partpurple_3.click = False
                screen.blit(game.partpurple_3.image, game.partpurple_3.rect)
                game.partpink_3.click = False
                screen.blit(game.partpink_3.image, game.partpink_3.rect)
                game.partorange_3.click = False
                screen.blit(game.partorange_3.image, game.partorange_3.rect)
                game.partgreen_3.click = False
                screen.blit(game.partgreen_3.image, game.partgreen_3.rect)

                print("rien ne se passe")
        elif event.type in (pg.KEYUP, pg.KEYDOWN):
                game.keys = pg.key.get_pressed()
                #pawn 2
        
    #updating pawns             
    game.pawn1.update(game.screen_rect)
    game.pawn2.update(game.screen_rect)
    game.pawn3.update(game.screen_rect)

    #updating camembert 1
    game.partblue_1.update(game.screen_rect)
    game.partyellow_1.update(game.screen_rect)
    game.partpurple_1.update(game.screen_rect)
    game.partpink_1.update(game.screen_rect)
    game.partorange_1.update(game.screen_rect)
    game.partgreen_1.update(game.screen_rect)

    #updating camembert 2
    game.partblue_2.update(game.screen_rect)
    game.partyellow_2.update(game.screen_rect)
    game.partpurple_2.update(game.screen_rect)
    game.partpink_2.update(game.screen_rect)
    game.partorange_2.update(game.screen_rect)
    game.partgreen_2.update(game.screen_rect)

    #updating camembert 2
    game.partblue_3.update(game.screen_rect)
    game.partyellow_3.update(game.screen_rect)
    game.partpurple_3.update(game.screen_rect)
    game.partpink_3.update(game.screen_rect)
    game.partorange_3.update(game.screen_rect)
    game.partgreen_3.update(game.screen_rect)
    #pg.display.update()
    game.clock.tick(game.fps)
