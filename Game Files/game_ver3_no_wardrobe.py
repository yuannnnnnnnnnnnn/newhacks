import pygame
from sys import exit
from random import randint
import end_screen

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            obstacle['rect'].x -= 5
            if obstacle['rect'].bottom == 320:
                screen.blit(rock_surface, obstacle['rect'])
            else:
                screen.blit(snowball_surf, obstacle['rect'])

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle['rect'].x > -200]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles, lives):
    new_obstacles = []
    for obstacle in obstacles:
        if player.colliderect(obstacle['rect']) and not obstacle['hit']:
            obstacle['hit'] = True
            lives -= 1
        if not obstacle['hit']:
            new_obstacles.append(obstacle)
    return new_obstacles, lives

def main():
    global screen, clock, rock_surface, snowball_surf, player_rect, coin_surf
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Do Not Leave Mike Naked')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font(None, 36)

    game_active = True
    coins = 0
    lives = 3

    # Load images and surfaces
    background_surface = pygame.image.load('background.jpg').convert()
    background_surface = pygame.transform.scale(background_surface, (WIDTH, HEIGHT))

    dirt_surf = pygame.image.load('dirt.png').convert_alpha()
    dirt_surf = pygame.transform.scale(dirt_surf, (620, 85))
    dirt_rect = dirt_surf.get_rect(bottomleft=(0, 400))

    coin_count_surf = test_font.render(str(coins), True, 'White')
    coin_count_rect = coin_count_surf.get_rect(topright=(545, 14))

    hearts_surf = pygame.image.load('heart.png').convert_alpha()
    hearts_surf = pygame.transform.scale(hearts_surf, (70, 35))

    corner_coin_surf = pygame.image.load('corner_coin.png').convert_alpha()
    corner_coin_surf = pygame.transform.scale(corner_coin_surf, (50, 30))
    corner_coin_rect = corner_coin_surf.get_rect(topright=(590, 10))

    coin_surf = pygame.image.load('coin.png').convert_alpha()
    coin_surf = pygame.transform.scale(coin_surf, (50, 30))
    coin_x_pos = 600

    # Obstacles
    rock_surface = pygame.image.load('better_rock.png').convert_alpha()
    rock_surface = pygame.transform.scale(rock_surface, (90, 50))

    snowball_surf = pygame.image.load('snowball.png').convert_alpha()
    snowball_surf = pygame.transform.scale(snowball_surf, (40, 40))

    obstacle_rect_list = []

    # Player
    player_surf = pygame.image.load('mike.png').convert_alpha()
    player_surf = pygame.transform.scale(player_surf, (40, 90))
    player_rect = player_surf.get_rect(midbottom=(80, 320))
    player_gravity = 0

    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 900)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 150:
                    player_gravity = -16

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 150:
                    player_gravity = -16

            if event.type == obstacle_timer and game_active:
                pass  # Add obstacle generation code here

        if game_active:
            if lives <= 0:
                game_active = False
        else:
            end_screen.ending_screen()
            main()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__": 
    main()
# if __name__ == "__main__":
#     main()
