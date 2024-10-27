import pygame
from sys import exit

pygame.init()
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Do Not Leave Mike Naked')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 36)

game_active = True

coins = 0
lives = 3

background_surface = pygame.image.load('background.jpg').convert()
background_surface = pygame.transform.scale(background_surface, (WIDTH, HEIGHT))

dirt_surf = pygame.image.load('dirt.png').convert_alpha()
dirt_surf = pygame.transform.scale(dirt_surf, (620, 110))
dirt_rect = dirt_surf.get_rect(bottomleft = (0, 400))

score_surf = test_font.render(str(coins), True, 'White')
score_rect = score_surf.get_rect(topright = (545, 14))

hearts_surf = pygame.image.load('heart.png').convert_alpha()
hearts_surf = pygame.transform.scale(hearts_surf, (70, 35))

coin_surf = pygame.image.load('coin.png').convert_alpha()
coin_surf = pygame.transform.scale(coin_surf, (50, 30))
coin_rect = coin_surf.get_rect(topright = (590,10))

rock_surface = pygame.image.load('better_rock.png').convert_alpha()
rock_surface = pygame.transform.scale(rock_surface, (90, 50))
rock_rect = rock_surface.get_rect(midbottom = (500, 320))

player_surf = pygame.image.load('mike.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (40, 90))
player_rect = player_surf.get_rect(midbottom = (80, 320))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos)  and player_rect.bottom >= 300: 
                player_gravity = -16

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -16
    
    if game_active:
        screen.blit(background_surface, (0,0))
        screen.blit(dirt_surf, dirt_rect)
        screen.blit(score_surf, score_rect)
        screen.blit(coin_surf, coin_rect)

        #hearts
        if lives == 3:
            screen.blit(hearts_surf, (0,10))
            screen.blit(hearts_surf, (50,10))
            screen.blit(hearts_surf, (100,10))
        elif lives == 2:
            screen.blit(hearts_surf, (0,10))
            screen.blit(hearts_surf, (50,10))
        elif lives == 1:
            screen.blit(hearts_surf, (0,10))
        else:
            game_active = False

        rock_rect.x -= 5
        if rock_rect.right <= 0: rock_rect.left = 600
        screen.blit(rock_surface, rock_rect)

        #Mike
        player_gravity += 0.7
        player_rect.y += player_gravity
        if player_rect.bottom >= 320: player_rect.bottom = 320
        screen.blit(player_surf, player_rect)

        #collision
        if rock_rect.colliderect(player_rect):
            lives -= 1
            rock_rect.left = 600
    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)