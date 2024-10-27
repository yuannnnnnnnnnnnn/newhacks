import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1300, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set width and height as needed
pygame.display.set_caption("Kitty Password Dress Up")

# Load and resize the background image
background_image = pygame.image.load("background.jpg")  # Replace with your image file
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load the image
image = pygame.image.load("mike.png")  # Replace with your image file path

# Resize the image
new_image_width, new_image_height = 200, 250  # Set your desired width and height
resized_image = pygame.transform.scale(image, (new_image_width, new_image_height))

# Set up fonts and colors
font = pygame.font.Font(None, 50)  # Use default font, size 36
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Text and typing variables
full_text = "Hey! I’m Mike, I lost all my clothes. BRRRRR it’s cold outside, please help me fetch some!"
displayed_text = ""
text_index = 0
typing_speed = 100  # in milliseconds

# Clock for timing
clock = pygame.time.Clock()
last_update_time = pygame.time.get_ticks()

# Run the game loop
running = True
while running:
    # Draw the background image
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the resized image
    screen.blit(resized_image, (100, 400))  # Adjust the (x, y) position as needed

    # Update the displayed text based on the typing speed
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > typing_speed and text_index < len(full_text):
        displayed_text += full_text[text_index]
        text_index += 1
        last_update_time = current_time

    # Render and display the text
    text_surface = font.render(displayed_text, True, WHITE)
    screen.blit(text_surface, (200, HEIGHT // 2))

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()

