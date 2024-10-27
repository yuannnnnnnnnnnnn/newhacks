import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('Do Not Leave Mike Naked')
clock = pygame.time.Clock()

background_surface = pygame.image.load('background.jpg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background_surface, (0,0))

    pygame.display.update()
    clock.tick(60)