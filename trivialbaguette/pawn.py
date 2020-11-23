import pygame as pg

# create classes to define different elements
class Pawn(pg.sprite.Sprite):

    def __init__(self,pos,nb):
        super().__init__()
        self.nb = nb;
        self.image = pg.image.load('assets/images/pawn'+str(self.nb)+'.png')
        self.image= pg.transform.scale(self.image, (75,70))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.rect.x = 800
        self.rect.y = 150*nb
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
    #def draw(self):
