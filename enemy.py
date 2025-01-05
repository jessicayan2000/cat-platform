import pygame
import time
# Object Oriented Programming (OOP): A way to organize code by using objects and class

# a class is a blueprint to something that you to make multiple copies of.
# Object: the thing that you make from the class (ex. an enemy made from enemies class)

class enemies:
  ''' constructor: make the objects of the class by starting off by creating it's main details'''
  def __init__(self, x, y, lv):
    self.green = pygame.image.load("images/green.png")
    self.green = pygame.transform.scale(self.green,(50,50))
    self.green_rect = self.green.get_rect()
    self.green_rect.x = x
    self.green_rect.y = y
    self.green2 = pygame.transform.flip(self.green, True, False)
    self.switch = True
    self.level = lv
    self.startpoint = 0
    self.stoppoint = 0 
    self.startTime = time.time()
  def movement(self):
    if self.level==1:
      self.startpoint = 50
      self.stoppoint = 10


    if self.green_rect.x >= self.startpoint:
      self.switch = False
      
    if self.green_rect.x <= self.stoppoint:
      self.switch = True
      
    if self.switch:
      self.green_rect.x += 3
    else:
      self.green_rect.x -= 3

  def health(self, wisp_rect, hp):
    currentTime = time.time()
    if wisp_rect.colliderect(self.green_rect):
      if currentTime - self.startTime >= 5:
        hp -= 10
        wisp_rect.x -= 20
        self.startTime = time.time()
        print(hp)
  
  def update(self,screen, wisp_rect, hp):
    if self.switch:
        screen.blit(self.green,self.green_rect)
    else:
        screen.blit(self.green2, self.green_rect)
        
    self.movement()
    self.health(wisp_rect, hp)