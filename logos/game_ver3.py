import pygame
from sys import exit

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Do Not Leave Mike Naked')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

background_surface = pygame.image.load('background.jpg')
text_surface = test_font.render('My game', True, 'Green')

rock_surface = pygame.image.load('rock.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background_surface, (0,0))
    screen.blit(text_surface, (230, 50))
    screen.blit(rock_surface, (0,0))

    pygame.display.update()
    clock.tick(60)