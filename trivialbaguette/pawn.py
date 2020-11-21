import pygame as pg

# create classes to define different elements
class Pawn(pg.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.init_state = 0;
        self.image = pg.image.load('assets/images/pawn2.png')
        self.image= pg.transform.scale(self.image, (55,50))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        #self.rect.x = 400
        #self.rect.y = 500
        self.click = False
        
    def check_click(self, pos):
        """
        This function is called from the event loop to check if a click
        overlaps with the player rect.
        pygame.mouse.get_rel must be called on an initial hit so that
        subsequent calls give the correct relative offset.
        """
        if self.rect.collidepoint(pos):
            self.click = True
            pg.mouse.get_rel()

    def update(self, screen_rect):
        """
        If the square is currently clicked, update its position based on the
        relative mouse movement.  Clamp the rect to the screen.
        """
        if self.click:
            self.rect.move_ip(pg.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
