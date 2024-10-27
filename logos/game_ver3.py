import pygame
from sys import exit
from random import randint

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
            obstacle['hit'] = True  # Mark as hit after the initial collision
            lives -= 1  # Decrease lives on first collision only
        if not obstacle['hit']:  # Only keep obstacles that haven't been hit
            new_obstacles.append(obstacle)
    return new_obstacles, lives  # Return filtered obstacle list and updated lives


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
dirt_surf = pygame.transform.scale(dirt_surf, (620, 85))
dirt_rect = dirt_surf.get_rect(bottomleft = (0, 400))

coin_count_surf = test_font.render(str(coins), True, 'White')
coin_count_rect = coin_count_surf.get_rect(topright = (530, 14))

hearts_surf = pygame.image.load('heart.png').convert_alpha()
hearts_surf = pygame.transform.scale(hearts_surf, (70, 35))

corner_coin_surf = pygame.image.load('corner_coin.png').convert_alpha()
corner_coin_surf = pygame.transform.scale(corner_coin_surf, (50, 30))
corner_coin_rect = corner_coin_surf.get_rect(topright = (590,10))

coin_surf = pygame.image.load('coin.png').convert_alpha()
coin_surf = pygame.transform.scale(coin_surf, (50, 30))
coin_x_pos = 600

#obstacles
rock_surface = pygame.image.load('better_rock.png').convert_alpha()
rock_surface = pygame.transform.scale(rock_surface, (90, 50))
rock_rect = rock_surface.get_rect(midbottom = (randint(600,800), 320))

snowball_surf = pygame.image.load('snowball.png').convert_alpha()
snowball_surf = pygame.transform.scale(snowball_surf, (40, 40))

obstacle_rect_list = []

player_surf = pygame.image.load('mike.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (40, 90))
player_rect = player_surf.get_rect(midbottom = (80, 320))
player_gravity = 0

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

restart_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 100, 50)

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
            if randint(0, 2):
                obstacle_rect_list.append({'rect': rock_surface.get_rect(midbottom=(randint(800, 1200), 320)), 'hit': False})
            else:
                obstacle_rect_list.append({'rect': snowball_surf.get_rect(midbottom=(randint(800, 1200), 220)), 'hit': False})
            pygame.time.set_timer(obstacle_timer, randint(1000, 1500))

    if game_active:
        screen.blit(background_surface, (0,0))
        #screen.blit(dirt_surf, dirt_rect)
        pygame.draw.rect(screen,(56, 60, 75), dirt_rect)
        screen.blit(coin_count_surf, coin_count_rect)
        screen.blit(corner_coin_surf, corner_coin_rect)

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

        coin_x_pos -=4
        if coin_x_pos < -100: coin_x_pos = 800
        screen.blit(coin_surf, (coin_x_pos, 250))

        if player_rect.colliderect(pygame.Rect(coin_x_pos, 250, coin_surf.get_width(), coin_surf.get_height())):
            coins += 1  # Increase coin count
            coin_x_pos = 770  # Reset coin position to right side
            # Update coin count display
            coin_count_surf = test_font.render(str(coins), True, 'White')

        #Mike
        player_gravity += 0.75
        player_rect.y += player_gravity
        if player_rect.bottom >= 320: player_rect.bottom = 320
        screen.blit(player_surf, player_rect)

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        obstacle_rect_list, lives = collisions(player_rect, obstacle_rect_list, lives)

    else:
        # screen.fill((239, 171, 235))
        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80, 320)
        # player_gravity = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button_rect.collidepoint(event.pos):
                # Reset game state
                game_active = True
                lives = 3
                obstacle_rect_list.clear()
                player_rect.midbottom = (80, 320)
                player_gravity = 0
    if game_active:
        pass

    else:
        # Draw the game-over screen
        screen.fill((239, 171, 235))

        # Draw restart button
        pygame.draw.rect(screen, (255, 0, 0), restart_button_rect)
        restart_text = test_font.render("Restart", True, "White")
        screen.blit(restart_text, restart_text.get_rect(center=restart_button_rect.center))

    pygame.display.update()
    clock.tick(60)
