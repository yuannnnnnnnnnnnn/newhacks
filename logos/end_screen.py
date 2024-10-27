import pygame
import sys
import game_ver3_no_wardrobe

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Over")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

title_font = pygame.font.Font(None, 70)
button_font = pygame.font.Font(None, 50)

game_over_text = title_font.render("Game Over", True, BLACK)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

button_width, button_height = 200, 60
retry_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height)

retry_text = button_font.render("Retry", True, BLACK)

def ending_screen():
    running = True
    while running:
        screen.fill(WHITE)
        
        screen.blit(game_over_text, game_over_rect)
        pygame.draw.rect(screen, GRAY, retry_button)
        
        screen.blit(retry_text, (retry_button.x + (button_width - retry_text.get_width()) // 2,
                                 retry_button.y + (button_height - retry_text.get_height()) // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(event.pos):
                    running = False
                    game_ver3_no_wardrobe.main()

if __name__ == "__main__":
    ending_screen()
