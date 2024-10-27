import pygame
import sys

# Initialize Pygame
pygame.init()
from PIL import Image
import level1

# Set up display
WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kitty Password Game")

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
label_text = 'Design your kitty password?'

show_text2 = False
related = ['kitten', 'purr', 'meow', 'whiskers', 'claw', 'hiss']
label2_text = 'Hint: ' + str(related)

life_image = pygame.image.load("life.jpg")  # Replace with your image file
life_image = pygame.transform.scale(life_image, (50, 50))

# Set initial number of lives
lives = 3  # Start with 3 lives

# Position for lives
life_spacing = 10  # Space between each life icon
life_start_x = 20  # Starting x position for the first life icon
life_y = 20  # y position for all life icons



# Main game loop
while True:
    window.fill(WHITE)
    # Event handling

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        cat_breeds = ['ragdoll', 'burmilla', 'siberian', 'tonkinese']

        # Handle keydpresses

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:  # Enter key clears the input
                if len(text) < 6:  # Change the label only when typing starts
                    label_text = "The length has to be at least 6..."
                    show_image = False
                    show_text2 = False
                elif not any([i in text for i in level1.words_related]):
                    label_text = 'The password must have one of the hint words'
                    show_image = False
                    show_text2 = True
                    lives -= 1
                elif sum([int(x) for x in text if x in numbers]) != 6:
                    label_text = 'The sum of the digits in the password must equal the number of cats in the photo'
                    show_image = True
                    show_text2 = False
                else:
                    label_text = 'Wow! Your password is PURRFECT'
                    show_image = False
                    show_text2 = False

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
    label_surface = font.render(label_text, True, (0, 0, 0))  # Black text
    window.blit(label_surface, (50, 250))

    if show_text2:
        label2_surface = font.render(label2_text, True, (0,0,0))
        window.blit(label2_surface, (50, 230))


    # Render and display the typed text inside the input box
    text_surface = font.render(text, True, BLACK)
    window.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    if show_image:
        if frame_count > 0:
            window.blit(gif_frames[current_frame], (800, 200))  # Adjust position as needed
            current_frame = (current_frame + 1) % frame_count

    for i in range(3):
        x = life_start_x + i * (life_image.get_width() + life_spacing)
        window.blit(life_image, (x, life_y))

    # Refresh display
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Set frame rate
