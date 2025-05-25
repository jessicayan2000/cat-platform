import pygame 
class health:
    def __init__(self):
        self.health = pygame.image.load("images/pixel_healthbar1.png")
        self.health = pygame.transform.scale(self.health, (100, 25))
        self.health_rect = self.health.get_rect() 
        self.health_rect.x = 10
        self.health_rect.y = 10
    
    def change_health(self):
        pass
    
    def update(self,screen):
        screen.blit(self.health,self.health_rect)
        