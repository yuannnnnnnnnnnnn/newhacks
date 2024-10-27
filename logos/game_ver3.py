import pygame
from sys import exit

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Do Not Leave Mike Naked')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 36)

coins = 0

background_surface = pygame.image.load('background.jpg').convert()
background_surface = pygame.transform.scale(background_surface, (WIDTH, HEIGHT))

score_surf = test_font.render(str(coins), True, 'White')
score_rect = score_surf.get_rect(topright = (545, 14))

hearts_surf = pygame.image.load('heart.png').convert_alpha()
hearts_surf = pygame.transform.scale(hearts_surf, (70, 35))

coin_surf = pygame.image.load('coin.png').convert_alpha()
coin_surf = pygame.transform.scale(coin_surf, (50, 30))
coin_rect = coin_surf.get_rect(topright = (590,10))

rock_surface = pygame.image.load('better_rock.png').convert_alpha()
rock_surface = pygame.transform.scale(rock_surface, (70, 35))
rock_rect = rock_surface.get_rect(midbottom = (500, 370))

player_surf = pygame.image.load('mike.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (60, 100))
player_rect = player_surf.get_rect(midbottom = (80, 370))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')
    
    screen.blit(background_surface, (0,0))
    screen.blit(score_surf, score_rect)
    screen.blit(coin_surf, coin_rect)
    screen.blit(hearts_surf, (0,10))
    screen.blit(hearts_surf, (50,10))
    screen.blit(hearts_surf, (100,10))
    rock_rect.x -= 4
    if rock_rect.right <= 0: rock_rect.left = 600
    screen.blit(rock_surface, rock_rect)
    screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)