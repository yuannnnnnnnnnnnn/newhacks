import pygame
import sys

# Initialize Pygame
pygame.init()
from PIL import Image

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Password Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (215, 176, 245)

show_image = False

def load_gif_frames(gif_path, size=(100, 100)):  # Set default size to 100x100 pixels
    with Image.open(gif_path) as img:
        frames = []
        try:
            while True:
                frame = img.copy()
                # Resize the frame before converting to Pygame format
                resized_frame = frame.resize(size, Image.LANCZOS)  # Use LANCZOS for high-quality resizing
                frames.append(pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode))
                img.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass  # End of GIF
    return frames

gif_frames = load_gif_frames("cat-cats.gif", size=(150, 150))  # Change size as needed

current_frame = 0
frame_count = len(gif_frames)
clock = pygame.time.Clock()  # Control frame rate

# Fonts
font = pygame.font.Font(None, 25)

# Text input variables
text = ""  # Stores the text that the player types
input_box = pygame.Rect(50, HEIGHT // 2 - 25, 500, 50)  # Rectangle for the text box
active = True  # Track whether input box is active
label_text = 'What is your password?'

# Main game loop
while True:
    window.fill(WHITE)
    # Event handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        # Handle keypresses

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:  # Enter key clears the input
                if len(text) < 6:  # Change the label only when typing starts
                    label_text = "The length has to be at least 6..."
                    show_image = False
                elif 'cat' not in text:
                    label_text = 'The password must contain the word "cat"'
                    show_image = False
                elif sum([int(x) for x in text if x in numbers]) != 6:
                    label_text = 'The sum of the digits in the password must equal the number of cats in the photo'
                    show_image = True
                else:
                    label_text = 'success'
                    show_image = False

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

    if show_image:
        if frame_count > 0:
            window.blit(gif_frames[current_frame], (600, 200))  # Adjust position as needed
            current_frame = (current_frame + 1) % frame_count

    # Refresh display
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Set frame rate
# yuan's change
