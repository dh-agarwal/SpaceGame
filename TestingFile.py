import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('astronaut.jpg')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 100
playerY = 100
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

#background
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (800,800))

# Planets
sun1 = pygame.image.load('sun.png')
sun1 = pygame.transform.scale(sun1, (150, 150))
sunX = 350
sunY = 250

planet_redblue1 = pygame.image.load('planet_redblue.png')
planet_redblue1 = pygame.transform.scale(planet_redblue1, (50, 50))
planet_redblueX = 370
planet_redblueY = 480

planet_green1 = pygame.image.load('planet_green.png')
planet_green1 = pygame.transform.scale(planet_green1, (50, 50))
planet_greenX = 370
planet_greenY = 400

planet_ring1 = pygame.image.load('planet_ring.png')
planet_ring1 = pygame.transform.scale(planet_ring1, (75, 50))
planet_ringX= 370
planet_ringY = 480

def background():
    screen.blit(bg, (0,0))

def sun():
    screen.blit(sun1, (sunX, sunY))

def planet_redblue():
    screen.blit(planet_redblue1, (planet_redblueX, planet_redblueY))

def planet_green():
    screen.blit(planet_green1, (planet_greenX, planet_greenY))

def planet_ring():
    screen.blit(planet_ring1, (planet_ringX, planet_ringY))

# Collision
def isCollision(playerX, playerY, planetX, planetY):
    if playerX > planetX - 10 and playerX < planetX + 10 and playerY > planetY - 10 and playerY < planetY + 10:
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

running = True
while running:
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
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = 0.5
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

    background()
    player(playerX, playerY)
    sun()     
    planet_redblue()
    planet_green()
    planet_ring()
    pygame.display.update()
