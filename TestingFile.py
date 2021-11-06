import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('astronaut.jpg')
pygame.display.set_icon(icon)

# Planets
planetImg = pygame.image.load('astronaut.jpeg')
planetX = 370
planetY = 480

def planet():
    screen.blit(planetImg, (planetX, planetY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    planet()
    pygame.display.update()
