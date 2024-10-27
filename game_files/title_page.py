# Import your game and shop modules
import pygame
import sys
import game_ver3
import wardrobe

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Title Screen")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Fonts
title_font = pygame.font.Font(None, 70)
button_font = pygame.font.Font(None, 50)

# Title text
title_text = title_font.render("Don't Leave Mike Naked!", True, BLACK)
title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

# Button settings
button_width, button_height = 200, 60
start_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height, button_width, button_height)
wardrobe_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 20, button_width, button_height)

# Button text
start_text = button_font.render("Start Game", True, BLACK)
wardrobe_text = button_font.render("Wardrobe", True, BLACK)

# Load the image
image = pygame.image.load("mike.png")  # Replace with your actual file name
image_rect = image.get_rect(bottomright=(600, 500))  # Position the image

def title_screen():
    while True:
        screen.fill(WHITE)
        
        # Draw title and image
        screen.blit(image, image_rect)  # Display the image
        screen.blit(title_text, title_rect)
        
        # Draw buttons
        pygame.draw.rect(screen, GRAY, start_button)
        pygame.draw.rect(screen, GRAY, wardrobe_button)
        
        # Draw button text
        screen.blit(start_text, (start_button.x + (button_width - start_text.get_width()) // 2,
                         start_button.y + (button_height - start_text.get_height()) // 2))
        screen.blit(wardrobe_text, (wardrobe_button.x + (button_width - wardrobe_text.get_width()) // 2,
                        wardrobe_button.y + (button_height - wardrobe_text.get_height()) // 2))

        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    game_ver3.start()  # Call the start function from the game module
                elif wardrobe_button.collidepoint(event.pos):
                    wardrobe.enter()  # Call the enter function from the shop module
        
        pygame.display.flip()

# Run the title screen
title_screen()
