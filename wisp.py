import pygame

class wisp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/walking/orange_cat1.png")  # image of cat
        self.image = pygame.transform.scale(wisp, (50, 50))  # how big cat is
        self.rect = wisp.get_rect()  # this creates rectangle/hitbox around the cat
        self.rect.x = 200
        self.rect.y = 210

    def update(self,screen):
        screen.blit(self.wisp,self.wisp_rect)