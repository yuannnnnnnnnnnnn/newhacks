import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Password Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (215, 176, 245)

image = pygame.image.load("campcat10.gif")  # Replace with your image file
image_rect = image.get_rect()
image_rect.topleft = (600, 400)

new_width, new_height = image.get_width() // 2, image.get_height() // 2
resized_image = pygame.transform.scale(image, (new_width, new_height))
show_image = False

# Fonts
font = pygame.font.Font(None, 25)

# Text input variables
text = ""  # Stores the text that the player types
input_box = pygame.Rect(50, HEIGHT // 2 - 25, 500, 50)  # Rectangle for the text box
active = True  # Track whether input box is active
label_text = 'What is your password?'

        # Handle mouse click
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # If the user clicks on the input box, activate it.
        #     if len(text) < 6:  # Change the label only when typing starts
        #         label_text = "The length has to be at least 6..."
        #     else:
        #         active = False

# Main game loop
while True:
    window.fill(WHITE)
    # Event handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle keypresses

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:  # Enter key clears the input
                if len(text) < 6:  # Change the label only when typing starts
                    label_text = "The length has to be at least 6..."
                    show_image = False
                elif 'cat' not in text:
                    label_text = 'The password must contain the word "cat"'
                    show_image = False
                elif 'cat' in text:
                    label_text = 'The sum of the digits in the password must equal the number of cats'
                    show_image = True
                elif sum([x for x in text if type(x) == int]) != 10:
                    label_text = 'The sum of the digits in the password must equal the number of cats in the photo'
                    show_image = False
                else:
                    label_text = 'success'

            elif event.key == pygame.K_BACKSPACE:  # Backspace deletes one character
                text = text[:-1]
                if text == "":
                    label_text = "Start typing your message..."  # Reset label if all text is deleted
            else:
                text += event.unicode  # Add the typed character to the text
                label_text = "Press enter to submit"

    # Draw the input box
    pygame.draw.rect(window, PURPLE, input_box, 2)

    # Render and display the label text above the input box
    label_surface = font.render(label_text, True, BLACK)
    window.blit(label_surface, (input_box.x, input_box.y - 40))  # Place text in the box

    # Render and display the typed text inside the input box
    text_surface = font.render(text, True, BLACK)
    window.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    # Draw the image on the screen
    if show_image:
        window.blit(resized_image, image_rect)

    # Refresh display
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Set frame rate
#lan's change test
# Yuan's chagne
##3# sdlfsldkjf




######meoww
# tooooooooooooooooooooooooooooooo
