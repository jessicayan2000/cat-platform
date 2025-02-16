import pygame

class platforms:    
    def __init__(self, x,y):
        self.platform = pygame.image.load("images/platforms/platform.png")
        self.platform = pygame.transform.scale(self.platform,(100,50))
        self.rect = self.platform.get_rect(topleft = (x,y))

    
    
    def update(self,screen):
        screen.blit(self.platform,self.rect)
