import pygame
from sys import exit

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Do Not Leave Mike Naked')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

background_surface = pygame.image.load('background.jpg').convert()
background_surface = pygame.transform.scale(background_surface, (WIDTH, HEIGHT))

text_surface = test_font.render('My game', True, 'Green')

rock_surface = pygame.image.load('better_rock.png').convert_alpha()
rock_surface = pygame.transform.scale(rock_surface, (70, 35))
rock_x_pos = 500

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background_surface, (0,0))
    screen.blit(text_surface, (230, 50))
    rock_x_pos -= 4
    if rock_x_pos < -100: rock_x_pos = 600
    screen.blit(rock_surface, (rock_x_pos,320))

    pygame.display.update()
    clock.tick(60)