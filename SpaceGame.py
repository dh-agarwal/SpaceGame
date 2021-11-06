import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('astronaut.jpg')
pygame.display.set_icon(icon)
pygame.font.init()
fontdodgeGame = pygame.font.SysFont('Comic Sans MS', 30)

# Player
playerImg = pygame.image.load('spaceship.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerImg1 = playerImg
playerX = 100
playerY = 100
playerX_change = 0
playerY_change = 0

# Player facing
playerImgLeft = pygame.transform.rotate(playerImg, 270)
playerImgRight = pygame.transform.rotate(playerImg, 90)
playerImgTop = pygame.transform.rotate(playerImg, 0)
playerImgDown = pygame.transform.rotate(playerImg, 180)

def player(x, y):
    screen.blit(playerImg1, (x, y))

#background
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (1200,700))

#music
mixer.music.load('bgmusic.mp3')
mixer.music.play(-1)

# Planets
sun1 = pygame.image.load('sun.png')
sun1 = pygame.transform.scale(sun1, (250, 250))
sunX = 470
sunY = 260

planet_green1 = pygame.image.load('planet_green.png')
planet_green1 = pygame.transform.scale(planet_green1, (75, 75))
planet_greenX = 580
planet_greenY = 80

planet_redblue1 = pygame.image.load('planet_redblue.png')
planet_redblue1 = pygame.transform.scale(planet_redblue1, (70, 70))
planet_redblueX = 350
planet_redblueY = 525

planet_ring1 = pygame.image.load('planet_ring.png')
planet_ring1 = pygame.transform.scale(planet_ring1, (110, 65))
planet_ringX = 800
planet_ringY = 530

earth1 = pygame.image.load('earth.png')
earth1 = pygame.transform.scale(earth1, (30, 30))
earthX = 20
earthY = 20

def background():
    screen.blit(bg, (0,0))

def sun(size):
    screen.blit(pygame.transform.scale(sun1, (size, size)), (sunX, sunY))

def planet_redblue():
    screen.blit(planet_redblue1, (planet_redblueX, planet_redblueY))

def planet_green():
    screen.blit(planet_green1, (planet_greenX, planet_greenY))

def planet_ring():
    screen.blit(planet_ring1, (planet_ringX, planet_ringY))
    
def earth():
    screen.blit(earth1, (earthX, earthY))

# Collision
def isCollision(playerX, playerY, planetX, planetY):
    if playerX > planetX - 40 and playerX < planetX + 40 and playerY > planetY - 40 and playerY < planetY + 40:
        return True
    return False

def waterGame():
    running = True
    while running:
        screen.fill((255,255,255))
        textsurface = fontdodgeGame.render('Some Text', False, (0, 0, 0))
        screen.blit(textsurface,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()

counter = 0
counter2 = 240

running = True
while running:
    counter=counter+1
    screen.fill((0,0,0))
    collision_redblue = isCollision(playerX, playerY, planet_redblueX, planet_redblueY)
    collision_green = isCollision(playerX, playerY, planet_greenX, planet_greenY)
    collision_ring = isCollision(playerX, playerY, planet_ringX, planet_ringY)

    if collision_ring:
        waterGame()
        playerX = 100
        playerY = 100
    elif collision_green:
        print('Collided with the green planet!')
    elif collision_redblue:
        print('Collided with the redblue planet!')

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                playerX_change = -2
                playerImg1 = playerImgRight
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
                playerImg1 = playerImgLeft
            if event.key == pygame.K_UP:
                playerY_change = -2
                playerImg1 = playerImg
            if event.key == pygame.K_DOWN:
                playerY_change = 2
                playerImg1 = playerImgDown
                
        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0
            
        #c_x, c_y = pygame.mouse.get_pos()
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #if (((650-c_x)**2+(450-c_y)**2) < 2500):

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1150:
        playerX = 1150

    if playerY <= 0:
        playerY = 0
    elif playerY >= 650:
        playerY = 650
        
    #planetmovement  
    if(counter%400 > 200):
        planet_greenX=planet_greenX+.3
    else:
        planet_greenX=planet_greenX-.3
    if(counter%300 > 150):
        planet_redblueX=planet_redblueX-.4
        planet_redblueY=planet_redblueY-.4
    else:        
        planet_redblueX=planet_redblueX+.4
        planet_redblueY=planet_redblueY+.4
    if(counter%600 > 300):
        counter2=counter2+.03
        planet_ringX=planet_ringX+.2
        planet_ringY=planet_ringY-.2
    else:
        counter2=counter2-.03
        planet_ringX=planet_ringX-.2
        planet_ringY=planet_ringY+.2
        
    if (counter == 1200):
        counter = 0
            
    background()    
    sun(counter2)     
    planet_redblue()
    planet_green()
    planet_ring()
    earth()
    player(playerX, playerY)
    pygame.display.update()
