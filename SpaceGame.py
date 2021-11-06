import pygame

pygame.init()

screen = pygame.display.set_mode((1300,900))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('astronaut.jpg')
pygame.display.set_icon(icon)

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
bg = pygame.transform.scale(bg, (1300,900))

# Planets
sun1 = pygame.image.load('sun.png')
sun1 = pygame.transform.scale(sun1, (250, 250))
sunX = 510
sunY = 355

planet_green1 = pygame.image.load('planet_green.png')
planet_green1 = pygame.transform.scale(planet_green1, (100, 100))
planet_greenX = 580
planet_greenY = 120

planet_redblue1 = pygame.image.load('planet_redblue.png')
planet_redblue1 = pygame.transform.scale(planet_redblue1, (70, 70))
planet_redblueX = 330
planet_redblueY = 700

planet_ring1 = pygame.image.load('planet_ring.png')
planet_ring1 = pygame.transform.scale(planet_ring1, (110, 65))
planet_ringX = 850
planet_ringY = 700

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

# Collision
def isCollision(playerX, playerY, planetX, planetY):
    if playerX > planetX - 30 and playerX < planetX + 30 and playerY > planetY - 30 and playerY < planetY + 30:
        return True
    return False

def newCanvas():
    running = True
    while running:
        screen.fill((0,255,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()
        
def movePlanet(pl):
    for x in range (0,50):
        planet_greenX=planet_greenX+1
        planet_greenY=planet_greenY+1
    for z in range(0,50):
        planet_greenX=planet_greenX-1
        planet_greenY=planet_greenY-1


running = True
counter = 0
counter2 = 240
while running:
    counter=counter+1
    screen.fill((0,0,0))
    collision_redblue = isCollision(playerX, playerY, planet_redblueX, planet_redblueY)
    collision_green = isCollision(playerX, playerY, planet_greenX, planet_greenY)
    collision_ring = isCollision(playerX, playerY, planet_ringX, planet_ringY)

    if collision_redblue:
        newCanvas()
        playerX = 100
        playerY = 100
    elif collision_green:
        print('Collided with the green planet!')
    elif collision_ring:
        print('Colliede with the ring planet!')

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

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750

    if playerY <= 0:
        playerY = 0
    elif playerY >= 750:
        playerY = 750
        
    #planetmovement  
    if(counter%400 > 200):
        planet_greenX=planet_greenX+.3
    else:
        planet_greenX=planet_greenX-.3
    if(counter%300 > 150):
        planet_redblueX=planet_redblueX-.4
        planet_redblueY=planet_redblueY+.4
    else:        
        planet_redblueX=planet_redblueX+.4
        planet_redblueY=planet_redblueY-.4
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
    player(playerX, playerY)
    pygame.display.update()
