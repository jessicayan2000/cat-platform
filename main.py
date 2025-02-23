import time, os
import pygame, sys
from enemy import enemies
from platform_1 import platforms
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
'''  


   Traffic cone 
         ^


     Tall hat
         _
        | |
        | |
        | |
        | |
      __|_|__
     >(^o.o^)<
       =>*<=  
       
        I
<=======o----
        I   
'''
wisp = pygame.image.load(
    "images/walking/catwalk0.png").convert_alpha()  # image of cat
wisp = pygame.transform.scale(wisp, (50, 50))  # how big cat is
wisp_rect = wisp.get_rect()  # this creates rectangle/hitbox around the cat
wisp_rect.x = 200
wisp_rect.y = 210

tree = pygame.image.load("images/mondstatTree.png")
tree = pygame.transform.scale(tree, (400, 300))
grass = pygame.image.load("images/grass_block.png")
grass = pygame.transform.scale(grass, (400, 50))
grass_rect = grass.get_rect()
grass_rect.x = 0
grass_rect.y = 250
clock = pygame.time.Clock()
gravity = 0
velocity = 0
isJump = True


enemies_list = []
platform_list = []
#      LEVELS
#------------------


     #Platforms:
platform1 = platforms(20, 150)
platform2 = platforms(100, 100)
platform3 = platforms(180, 70)
platform4 = platforms(270,150)
platform5 = platforms(190, 60)
platform6 = platforms(15, 60)

platforms = [platform1, platform2, platform3, platform4, platform5, platform6]

     #Enemies:
enemy1 = enemies(30,130,1)


# LEVEL 1 Platforms
#------------------
def lv1():
     platform_list.clear()
     platform_list.append(platform1)
     platform_list.append(platform2)
     platform_list.append(platform3)
     enemies_list.clear()
     enemies_list.append(enemy1)




# LEVEL 2 platforms
#-------------------
def lv2():
     platform_list.clear()
     platform_list.append(platform2)
     platform_list.append(platform4)
     platform_list.append(platform5)
     platform_list.append(platform6)


# LEVEL 3 platforms
#-------------------
def lv3():
     platform_list.append(platform5)
     platform_list.append(platform1)
     platform_list.append(platform4)

lv2()
#-------------------

onPlatform = False



          

def jump():
     global velocity, gravity,grass_rect, jumps
     velocity += gravity  # subtract velocity from gravity to slow down velocity
     wisp_rect.y  -= velocity  # makes us go up by velocity
     
     if wisp_rect.colliderect(grass_rect):
          velocity = 0
          gravity = 0 
          grass_rect.y = 250
          jumps = 3 

          
          
          
          

    

startingTime = time.time()  # starting time for the walking animation
i = 0

# this is for the walking animation of your character
def walk():
     global i, startingTime, wisp
     currentTime = time.time()
     walking = ["catwalk0.png", "catwalk1.png", "catwalk2.png", "catwalk3.png"]
     wisp = pygame.image.load("images/walking/" + walking[i]).convert_alpha()
     if i != 0:
          wisp = pygame.transform.scale(wisp, (50, 50))
     else:
          wisp = pygame.transform.scale(wisp, (50, 65))

     if currentTime - startingTime >= 0.2:
          i += 1
          startingTime = time.time()

     if i > 3:
          i = 0

# this is for backwards walking animation
def revWalk():
     global i, startingTime, wisp
     currentTime = time.time()
     walking = ["catwalk0.png", "catwalk1.png", "catwalk2.png", "catwalk3.png"]
     wisp = pygame.image.load("images/walking/" + walking[i]).convert_alpha()
     wisp = pygame.transform.flip(wisp, True, False)
     if i != 0:
          wisp = pygame.transform.scale(wisp, (50, 50))
     else:
          wisp = pygame.transform.scale(wisp, (50, 65))
 
     if currentTime - startingTime >= 0.2:
          i += 1
          startingTime = time.time()

     if i > 3:
          i = 0
          
# this is set to zero just so you can jump automatically when you start the game
jumps= 3
startTime = 0
hp = 4000
while True:
     if isJump:
          jump()
     
     screen.fill("gray")
     currentTime = time.time()


     key = pygame.key.get_pressed()
     if key[pygame.K_a]:
          wisp_rect.x -= 5
          walk()
     if key[pygame.K_d]:
          wisp_rect.x += 5
          revWalk()

     if key[pygame.K_SPACE] and jumps:
          if (wisp_rect.colliderect(grass_rect) or  (velocity >= -4 and velocity <= 4)) or currentTime-startTime >= 16:
               gravity = -2
               velocity = 30
               wisp_rect.y -= 10
               startTime = time.time()
               jumps-=1
               

     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               sys.exit()
     

     screen.blit(tree, (0, 0))
     screen.blit(grass, grass_rect)
     screen.blit(wisp, wisp_rect)

     # updating platforms 
     for platform in platform_list:
          platform.update(screen)
     
     
     for platforms in platform_list:
          if wisp_rect.colliderect(platforms) and velocity <=0:
               velocity = 0
               gravity = 0
               jumps = 3
          elif wisp_rect.colliderect(platforms) == False and velocity == 0 and (wisp_rect.colliderect(grass_rect) == False):
               gravity = -2 

     # updating enemies
     for enemies in enemies_list:
          if enemies.update(screen, wisp_rect):
               hp -= 10
     
   
     clock.tick(15)
     pygame.display.update()
