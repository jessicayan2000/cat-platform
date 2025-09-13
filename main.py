import time, os
import pygame, sys
from enemy import enemies
from platform_1 import platforms
from pygame.locals import QUIT
from health import health
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
        | |
        | |
        | |
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
        
         ^
       /___\            
     >(^o.o^)<        
     Wizard cat        
        
'''
wisp = pygame.image.load(
    "images/walking/orange_cat1.png").convert_alpha()  # image of cat
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

health_bar1 = health()
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

platforms = [platform1, platform2, platform3, platform4, platform5, platform6, grass_rect]

     #Enemies:
enemy1 = enemies(30,130,1)
enemy2 = enemies(100,40,2)

# LEVEL 1 Platforms
#------------------
def lv1():
     platform_list.clear()
     platform_list.append(platform1)
     platform_list.append(platform2)
     platform_list.append(platform3)
     platform_list.append(grass_rect)
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
     platform_list.append(grass_rect)
     enemies_list.clear()
     enemies_list.append(enemy2)

# LEVEL 3 platforms
#-------------------
def lv3():
     platform_list.clear()
     platform_list.append(platform5)
     platform_list.append(platform1)
     platform_list.append(platform4)
     platform_list.append(grass_rect)
     enemies_list.clear()
     enemies_list.append(enemy1)
#-------------------

onPlatform = False

levels = [lv1(), lv2(), lv3()]

          
          
def jump():
     global velocity, gravity,grass_rect, jumps
     velocity += gravity  # subtract velocity from gravity to slow down velocity
     wisp_rect.y  -= velocity  # makes us go up by velocity
     
     for platform in platform_list:
          if wisp_rect.colliderect(platform) and velocity <= 0:
               velocity = 0
               velocity -= gravity
               grass_rect.y = 250
               jumps = 3
               if wisp_rect.colliderect(grass_rect):
                    wisp_rect.y = 210
     if velocity <= -30:
          velocity = -30
     
          
     
     
               
               
             


          
          
          
          
          

    

startingTime = time.time()  # starting time for the walking animation
i = 0

# this is for the walking animation of your character
def revWalk():
     global i, startingTime, wisp
     currentTime = time.time()
     walking = ["orange_cat4.png", "orange_cat1.png", "orange_cat2.png", "orange_cat3.png"]
     wisp = pygame.image.load("images/walking/" + walking[i]).convert_alpha()
     if i != 0:
          wisp = pygame.transform.scale(wisp, (45, 45))
     else:
          wisp = pygame.transform.scale(wisp, (45, 45))

     if currentTime - startingTime >= 0.2:
          i += 1
          startingTime = time.time()

     if i > 3:
          i = 0

# this is for backwards walking animation
def walk():
     global i, startingTime, wisp
     currentTime = time.time()
     walking = ["orange_cat4.png", "orange_cat1.png", "orange_cat2.png", "orange_cat3.png"]
     wisp = pygame.image.load("images/walking/" + walking[i]).convert_alpha()
     wisp = pygame.transform.flip(wisp, True, False)
     if i != 0:
          wisp = pygame.transform.scale(wisp, (45, 45))
     else:
          wisp = pygame.transform.scale(wisp, (45, 45))
 
     if currentTime - startingTime >= 0.2:
          i += 1
          startingTime = time.time()
          

     if i > 3:
          i = 0
          
healthTime = time.time() 
# this is set to zero just so you can jump automatically when you start the game
jumps= 3
startTime = 0
hp = 4000
collide = False
currentlevel = 1
while True:
     #print(hp)
     if isJump:
          jump()
     
     screen.fill("gray")
     currentTime = time.time()
     
     # if you go to the right, then go to next level
     if wisp_rect.x >= 370 and currentlevel < 3:
          currentlevel += 1
          wisp_rect.x = 0
     # if you go to the left, then go to the previous level
     elif wisp_rect.x <= 0 and currentlevel > 1:
          currentlevel -= 1
          wisp_rect.x = 370

     if currentlevel == 1:
          lv1()
          if wisp_rect.x <= 0:
               wisp_rect.x = 10
     if currentlevel == 2:
          lv2()
     if currentlevel == 3:
          lv3()
          if wisp_rect.x >=370:
               wisp_rect.x = 360

     key = pygame.key.get_pressed()
     if key[pygame.K_a] or key[pygame.K_LEFT]:
          wisp_rect.x -= 5
          walk()
     if key[pygame.K_d] or key[pygame.K_RIGHT]:
          wisp_rect.x += 5
          revWalk()

     if (key[pygame.K_SPACE] or key[pygame.K_UP] )and jumps:
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
     
     if wisp_rect.colliderect(enemy1.green_rect) and currentTime - healthTime >= 5:
          health_bar1.change_health()
          healthTime = time.time() 

     screen.blit(tree, (0, 0))
     screen.blit(grass, grass_rect)
     screen.blit(wisp, wisp_rect)
     pygame.draw.rect(screen, "yellow", wisp_rect, 5)
     
     health_bar1.update(screen) 
     
     # updating platforms 
     for platform in range(len(platform_list) - 1):
          platform_list[platform].update(screen)
          pygame.draw.rect(screen, "yellow", platform_list[platform].rect, 5)
          if wisp_rect.colliderect(platform_list[platform]) == True and velocity == 0 and (wisp_rect.colliderect(grass_rect) == False):
               if wisp_rect.colliderect(platform_list[platform]) and pygame.sprite.spritecollide(wisp, platform_list[plaform], 0, collide_mask):
                    collide = True
                    print("hi")
               else:
                    collide = False
     
     # updating enemies
     for enemies in enemies_list:
          if enemies.update(screen, wisp_rect):
               hp -= 10
     
   
     clock.tick(15)
     pygame.display.update()
