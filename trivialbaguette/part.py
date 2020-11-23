import pygame as pg

# create classes to define different elements
class Part(pg.sprite.Sprite):

    def __init__(self,pos,color,nb):
        super().__init__()
        #self.nb = nb;
        self.won = False
        self.image_empty = pg.image.load('assets/images/part'+color+'_1.png')
        self.image_empty = pg.transform.scale(self.image_empty, (55,50))
        self.image_full = pg.image.load('assets/images/part'+color+'_2.png')
        self.image_full = pg.transform.scale(self.image_full, (55,53))
        self.image = self.image_empty
        self.rect = self.image.get_rect()
        self.rect.center = pos
        if color == 'blue':
            self.rect.x = 910
            self.rect.y = 60+150*(nb-1)
        if color == 'yellow':
            self.rect.x = 949
            self.rect.y = 50+150*(nb-1)
        if color == 'purple':
            self.rect.x = 987
            self.rect.y = 60+150*(nb-1)
        if color == 'pink':
            self.rect.x = 986
            self.rect.y = 119+150*(nb-1)
        if color == 'orange':
            self.rect.x = 949
            self.rect.y = 129+150*(nb-1)
        if color == 'green':
            self.rect.x = 910
            self.rect.y = 119+150*(nb-1)
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
            self.won= not self.won

    def update(self, screen_rect):
        """
        If the square is currently clicked, update its position based on the
        relative mouse movement.  Clamp the rect to the screen.
        """
        if self.click:
            if self.won:
                self.image = self.image_full
            if not self.won:
                self.image = self.image_empty 
          
