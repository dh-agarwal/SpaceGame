import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("Space Game")
icon = pygame.image.load('astronaut.jpg')
pygame.display.set_icon(icon)

# Fonts
pygame.font.init()
font1 = pygame.font.SysFont('Papyrus', 40)

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

# Backgrounds
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (1200,700))

ocean = pygame.image.load("underwater.png")
ocean = pygame.transform.scale(ocean, (1200, 700))

# Music
mixer.music.load('bgmusic.mp3')
mixer.music.play(-1)

# Diver
diver1 = pygame.image.load('diver.png')
diver1 = pygame.transform.scale(diver1, (170,75))
diverX = 60
diverY = 400

# Sea Monsters
monst_1 = pygame.image.load('seamonst.png')
monst_1 = pygame.transform.scale(monst_1, (170,75))
monst1X = 800
monst1Y = 300

monst_2 = pygame.image.load('seamonst.png')
monst_2 = pygame.transform.scale(monst_2, (170,75))
monst2X = 800
monst2Y = 100

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

def diver():
    screen.blit(diver1, (diverX, diverY))
    
def seamonst1():
    screen.blit(monst_1, (monst1X, monst1Y))
    
def seamonst2():
    screen.blit(monst_2, (monst2X, monst2Y))
    
def background():
    screen.blit(bg, (0,0))

def oceanbg():
    screen.blit(ocean, (0,0))

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

# Game Over
def gameOver():
    running = True
    while running:
        screen.fill((255,255,255))
        text = font1.render('GOOD GAME. YOU DIED', True, (0, 0, 0))
        screen.blit(text,(240,80))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waterGame()
                    
        pygame.display.update()

# Water Game

def waterStart():
    running = True
    while running:
        screen.fill((0,0,0))
        oceanbg()
        textsurface = font1.render('Avoid the monsters by swimming around past them.', True, (0, 0, 0))
        textsurface2 = font1.render('Swim far enough to obtain a fuel tank.', True, (0, 0, 0))
        textsurface3 = font1.render('Click enter to start.', True, (0, 0, 0))
        screen.blit(textsurface,(240,80))
        screen.blit(textsurface2,(310,120))
        screen.blit(textsurface3,(420,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waterGame()
                    
        pygame.display.update()
        
def waterGame():
    running = True
    global diverX
    global diverY
    diverX = 60
    diverY = 400
    diverX_change = 0
    diverY_change = 0
    while running:
        screen.fill((0,0,0))
        oceanbg()
        diver()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    diverX_change = -.5
                if event.key == pygame.K_RIGHT:
                    diverX_change = .5
                if event.key == pygame.K_UP:
                    diverY_change = -2
                if event.key == pygame.K_DOWN:
                    diverY_change = 2
                    
            if event.type == pygame.KEYUP:
                diverX_change = 0
                diverY_change = 0
        
        diverX += diverX_change
        diverY += diverY_change
        diverX += .2
        
        if diverY <= 0:
            diverY = 0
        elif diverY >= 550:
            diverY = 550
            
        if diverX <= 0:
            diverX = 0
        
        pygame.display.update()

def bossGame():
    # Ship
    shipImg = pygame.image.load('spaceship.png')
    shipImg = pygame.transform.scale(shipImg, (50, 50))
    shipImg = pygame.transform.rotate(shipImg, 270)
    shipImg1 = shipImg
    shipX = 100
    shipY = 100
    shipX_change = 0
    shipY_change = 0

    def ship(x, y):
        screen.blit(shipImg1, (x, y))

    # Boss
    bossImg = pygame.image.load('alien.png')
    bossImg = pygame.transform.scale(bossImg, (200, 200))
    bossX = 990
    bossY = 200
    bossSpeed = 0.5

    def boss():
        screen.blit(bossImg, (bossX, bossY))

    # Projectile
    slimeImg = pygame.image.load('slime.png')
    slimeImg = pygame.transform.scale(slimeImg, (50, 50))
    slimeImg = pygame.transform.rotate(slimeImg, 90)
    slimeX = bossX
    slimeY = 0
    slimeDX = -1
    slimeDY = 0
    slime_state = "ready"

    def shoot_proj(x, y):
        global slime_state
        slime_state = "fire"
        screen.blit(slimeImg, (x - 50, y + 75))

    running = True
    while running:
        screen.fill((100,255,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_LEFT:
                    shipX_change = -1
                if event.key == pygame.K_RIGHT:
                    shipX_change = 1
                if event.key == pygame.K_UP:
                    shipY_change = -1
                if event.key == pygame.K_DOWN:
                    shipY_change = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    shipX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    shipY_change = 0
        
        if slimeX <= 0:
            slimeX = 940
            slime_state = "ready"

        if slime_state is "fire":
            shoot_proj(slimeX, bossY)
            slimeX += slimeDX

        if bossY == 400:
            slime_state = "fire"

        shipX += shipX_change
        shipY += shipY_change

        if shipX <= 0:
            shipX = 0
        elif shipX >= 1150:
            shipX = 1150

        if shipY <= 0:
            shipY = 0
        elif shipY >= 650:
            shipY = 650

        if bossY == 510 or bossY == 0:
            bossSpeed *= -1
            
        bossY += bossSpeed

        boss()
        ship(shipX, shipY)
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
        waterStart()
        playerX = 100
        playerY = 100
    elif collision_green:
        bossGame()
        playerX = 100
        playerY = 100
        playerX_change = 0
        playerY_change = 0 
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
