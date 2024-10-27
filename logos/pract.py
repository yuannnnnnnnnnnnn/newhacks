import pygame
import sys
from PIL import Image

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Password Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (215, 176, 245)

# Define game states
MAIN_MENU = "main_menu"
LEVEL_1 = "level_1"
current_state = MAIN_MENU  # Start on the main menu

# Button setup for main menu
button_width = 200
button_height = 50
buttons = [
    {"rect": pygame.Rect((WIDTH - button_width) // 2, 200, button_width, button_height), "label": "Go to Level 1", "state": LEVEL_1}
]

# Load GIF frames
def load_gif_frames(gif_path, size=(150, 150)):  # Set default size to 150x150 pixels
    with Image.open(gif_path) as img:
        frames = []
        try:
            while True:
                frame = img.copy()
                resized_frame = frame.resize(size, Image.LANCZOS)  # Resize frame
                frames.append(pygame.image.fromstring(resized_frame.tobytes(), resized_frame.size, resized_frame.mode))
                img.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass  # End of GIF
    return frames

gif_frames = load_gif_frames("cat-cats.gif", size=(150, 150))
current_frame = 0
frame_count = len(gif_frames)
clock = pygame.time.Clock()  # Control frame rate

# Fonts
font = pygame.font.Font(None, 25)

# Password game variables
text = ""  # Stores the text that the player types
input_box = pygame.Rect(50, HEIGHT // 2 - 25, 500, 50)  # Rectangle for the text box
active = True  # Track whether input box is active
label_text = 'What is your password?'

show_image = False
related = ['kitten', 'purr', 'meow', 'whiskers', 'claw', 'hiss']
label2_text = 'Hint: ' + str(related)

life_image = pygame.image.load("life.jpg")  # Replace with your image file
life_image = pygame.transform.scale(life_image, (50, 50))

# Set initial number of lives
lives = 3  # Start with 3 lives
life_spacing = 10  # Space between each life icon
life_start_x = 20  # Starting x position for the first life icon
life_y = 20  # y position for all life icons

def level_1_game():
    global text, show_image, lives, label_text, active, current_frame, frame_count

    window.fill(WHITE)  # Fill the background

    # Event handling for LEVEL_1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:  # Enter key clears the input
                if len(text) < 6:
                    label_text = "The length has to be at least 6..."
                    show_image = False
                elif not any([i in text for i in related]):
                    label_text = 'The password must have one of the hint words'
                    show_image = False
                    lives -= 1
                elif sum([int(x) for x in text if x in numbers]) != 6:
                    label_text = 'The sum of the digits in the password must equal 6'
                    show_image = True
                else:
                    label_text = 'Success!'
                    show_image = False

            elif event.key == pygame.K_BACKSPACE:  # Backspace deletes one character
                text = text[:-1]
                if text == "":
                    label_text = "Start typing your message..."  # Reset label if all text is deleted
            else:
                text += event.unicode  # Add the typed character to the text

    # Draw the input box
    pygame.draw.rect(window, PURPLE, input_box, 2)

    # Render and display the label text above the input box
    label_surface = font.render(label_text, True, (0, 0, 0))  # Black text
    window.blit(label_surface, (50, 250))

    # Render and display the typed text inside the input box
    text_surface = font.render(text, True, BLACK)
    window.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    if show_image:
        if frame_count > 0:
            window.blit(gif_frames[current_frame], (800, 200))  # Adjust position as needed
            current_frame = (current_frame + 1) % frame_count

    # Draw the lives
    for i in range(lives):
        x = life_start_x + i * (life_image.get_width() + life_spacing)
        window.blit(life_image, (x, life_y))

# Main game loop
while True:
    if current_state == MAIN_MENU:
        window.fill(WHITE)

        # Event handling for main menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        current_state = button["state"]  # Switch to the selected state

        # Draw buttons for the main menu
        for button in buttons:
            pygame.draw.rect(window, (173, 216, 230), button["rect"])  # Light blue
            pygame.draw.rect(window, BLACK, button["rect"], 2)  # Border

            # Render button text
            text_surface = font.render(button["label"], True, BLACK)
            text_x = button["rect"].x + (button["rect"].width - text_surface.get_width()) // 2
            text_y = button["rect"].y + (button["rect"].height - text_surface.get_height()) // 2
            window.blit(text_surface, (text_x, text_y))

    elif current_state == LEVEL_1:
        level_1_game()  # Call level 1 game logic

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Frame rate control
