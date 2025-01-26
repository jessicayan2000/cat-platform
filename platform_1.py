import pygame

class platforms:    
    def __init__(self, x,y):
        self.platform = pygame.image.load("images/platforms/platform.png")
        self.platform = pygame.transform.scale(self.platform,(100,50))
        self.platform_rect = self.platform.get_rect()
        self.platform_rect.x = x
        self.platform_rect.y = y
    
    
    def update(self,screen):
        screen.blit(self.platform,self.platform_rect)
