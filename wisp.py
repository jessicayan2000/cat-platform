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
        self.walking = False
        self.image = self.images["walking1"]  # image of cat
        self.rect = self.image.get_rect()  # this creates rectangle/hitbox around the cat
        self.rect.x = x
        self.rect.y = y
        self.t = 0

     def update(self, startingTime, currentTime):
          self.t += 1
          images = list(self.images.values())
          
          if self.walking:
               self.image = images[((self.t) % 4)]
    

     def revWalk(self, currentTime, startingTime):
          self.rect.x += 5
          self.walking = True

          if currentTime - startingTime >= 0.2:
               self.t += 1
               startingTime = time.time()

          

     # this is for backwards walking animation
     def walk(self, currentTime, startingTime):
          self.walking = True
          self.rect.x -= 5
     
          if currentTime - startingTime >= 0.2:
               self.t += 1
               startingTime = time.time()
               



