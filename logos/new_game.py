import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000, 800))  # Set width and height as needed
pygame.display.set_caption("Kitty Password Dress Up")

# Load the image
image = pygame.image.load("Standing_Cat")  # Replace with your image file path

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill((255, 255, 255))  # White background

    # Display the image
    screen.blit(image, (100, 100))  # Adjust the (x, y) position as needed

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
