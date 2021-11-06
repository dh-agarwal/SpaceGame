import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('astronaut.jpg')
pygame.display.set_icon(icon)

# Planets
planet_redblue1 = pygame.image.load('planet_redblue.png')
planet_redblue1 = pygame.transform.scale(planet_redblue1, (50, 50))

planet_frozen1 = pygame.image.load('planet_frozen.png')
planet_frozen1 = pygame.transform.scale(planet_frozen1, (50, 50))


def planet_redblue():
    screen.blit(planet_redblue1, (370, 480))

def planet_frozen():
    screen.blit(planet_frozen1, (370, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    planet_redblue()
    planet_frozen()
    pygame.display.update()
