import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('astronaut.jpg')
pygame.display.set_icon(icon)

#background
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (800,600))

# Planets
planet_redblue1 = pygame.image.load('planet_redblue.png')
planet_redblue1 = pygame.transform.scale(planet_redblue1, (50, 50))
planet_redblueX = 370
planet_redblueY = 480

planet_frozen1 = pygame.image.load('planet_frozen.png')
planet_frozen1 = pygame.transform.scale(planet_frozen1, (50, 50))
planet_frozenX = 370
planet_frozenY = 400

planet_ring = pygame.image.load('planet_ring.png')
planet_ring = pygame.transform.scale(planet_ring, (75, 50))
planet_ringX= 370
planet_ringY = 480

def background():
    screen.blit(bg, (0,0))

def planet_redblue():
    screen.blit(planet_redblue1, (planet_redblueX, planet_redblueY))

def planet_frozen():
    screen.blit(planet_frozen1, (planet_frozenX, planet_frozenY))

def planet_cracked():
    screen.blit(planet_ring, (planet_ringX, planet_ringY))

running = True
while running:
    screen.fill((0,0,0))
    planet_redblueX=planet_redblueX+1
    planet_frozenY=planet_frozenY-1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    background()       
    planet_redblue()
    planet_frozen()
    planet_cracked()
    pygame.display.update()
