# Import necessary modules
import pygame
import sys
import game_ver3_no_wardrobe  # Import the main game module

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
start_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height // 2, button_width, button_height)

# Button text
start_text = button_font.render("Start Game", True, BLACK)

# Load the image
image = pygame.image.load("mike.png")  # Ensure "mike.png" is in the same directory
image_rect = image.get_rect(bottomright=(600, 500))  # Position the image

def title_screen():
    running = True
    while running:
        screen.fill(WHITE)
        
        # Draw title and image
        screen.blit(image, image_rect)  # Display the image
        screen.blit(title_text, title_rect)
        
        # Draw the start button
        pygame.draw.rect(screen, GRAY, start_button)
        
        # Draw start button text
        screen.blit(start_text, (start_button.x + (button_width - start_text.get_width()) // 2,
                                 start_button.y + (button_height - start_text.get_height()) // 2))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    running = False  # Exit the title screen loop
                    game_ver3_no_wardrobe.main()  # Call the main function in your game file

# Run the title screen
if __name__ == "__main__":
    title_screen()
