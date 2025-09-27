import pygame
import time 

class wisp(pygame.sprite.Sprite):
    def __init__(self,x = 200, y =210):
        super().__init__()
        self.images = {
             f"walking{i}":pygame.image.load(f"images/walking/orange_cat{i}.png") for i in range (1,5)
        }
        for name, image in self.images.items():
             self.images[name] = pygame.transform.scale(image, (45, 45))
        self.image = self.images["walking1"]  # image of cat
        self.rect = self.image.get_rect()  # this creates rectangle/hitbox around the cat
        self.rect.x = x
        self.rect.y = y

def revWalk():
     global i, startingTime, self
     currentTime = time.time()
     walking = ["orange_cat4.png", "orange_cat1.png", "orange_cat2.png", "orange_cat3.png"]
     self.image = pygame.image.load("images/walking/" + walking[i]).convert_alpha()
     if i != 0:
          self.image = pygame.transform.scale(self.image, (45, 45))
     else:
          self.image = pygame.transform.scale(self.image, (45, 45))

     if currentTime - startingTime >= 0.2:
          i += 1
          startingTime = time.time()

     if i > 3:
          i = 0

# this is for backwards walking animation
def walk():
     global i, startingTime, self
     currentTime = time.time()
     walking = ["orange_cat4.png", "orange_cat1.png", "orange_cat2.png", "orange_cat3.png"]
     self.image = pygame.image.load("images/walking/" + walking[i]).convert_alpha()
     self.image = pygame.transform.flip(self.image, True, False)
     if i != 0:
          self.image = pygame.transform.scale(self.image, (45, 45))
     else:
          self.image = pygame.transform.scale(self.image, (45, 45))
 
     if currentTime - startingTime >= 0.2:
          i += 1
          startingTime = time.time()
          

     if i > 3:
          i = 0