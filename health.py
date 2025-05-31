import pygame 
import enum
class health:
    def __init__(self):
        self.health_images = ["images/pixel_healthbar1.png", "images/pixel_healthbar2.png", "images/pixel_healthbar3.png", "images/pixel_healthbar4.png", "images/pixel_healthbar5.png","images/pixel_healthbar6.png"]
        self.hp = 0
        # self.health = pygame.image.load(self.health_images[self.hp])
        self.health = pygame.transform.scale(pygame.image.load(self.health_images[self.hp]), (100, 25))
        self.health_rect = self.health.get_rect() 
        self.health_rect.x = 10
        self.health_rect.y = 10
        

        
    def change_health(self):
        #if the cat touches the slime, the healthbar should change to the next image until it runs out 
        self.hp = (self.hp + 1) % len(self.health_images)
    
    def update(self,screen):
        self.health = pygame.transform.scale(pygame.image.load(self.health_images[self.hp]), (100, 25))
        screen.blit(self.health,self.health_rect)
        