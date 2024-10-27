import pygame
from sys import exit

class Clothing:
    """Clothing object representing an item with status and price."""
    def __init__(self, name, category, color, x, y, width, height, image, price, cat_scale, position):
        self.name = name
        self.category = category
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(image, (width, height))
        self.price = price
        self.bought = False  # Tracks if the item is bought
        self.cat_image = pygame.transform.scale(image, cat_scale)  # Scale for cat display
        self.position = position  # Position for cat display

    def draw(self, screen, highlight=False):
        """Draw the clothing item with optional highlight."""
        border_color = (255, 215, 0) if highlight else self.color  # Gold border if highlighted
        pygame.draw.rect(screen, border_color, self.rect, 3)  # Draw border
        screen.blit(self.image, self.rect.topleft)  # Draw the image

    def draw_on_cat(self, screen):
        """Draw the clothing item on the cat."""
        screen.blit(self.cat_image, self.position)  # Draw the scaled image on the specified position


# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SHOP')
font = pygame.font.Font(None, 36)

# Load background and mike image
background_surf = pygame.image.load('blurred_background.png').convert()
background_surf = pygame.transform.scale(background_surf, (WIDTH, HEIGHT))
mike_image = pygame.image.load('mike.png').convert_alpha()

# Load clothing images
image_list = ['PMG mike jeans.png', 'PNG mike shorts.png', 'PNG mike baseball cap.png',
              'PNG mike beenie.png', 'PNG mike shirt.png', 'PNG mike sweater.png',
              'PNG mike tshirt.png', 'PNG mike tshirt.png']
clothes_images = [pygame.image.load(image).convert_alpha() for image in image_list]

# Define scales for each category
HAT_SCALE = (80, 80)  # Smaller size for hats
PANTS_SCALE = (110, 110)  # Larger size for pants
TOP_SCALE = (150, 120)  # Custom size for tops

# Define positions for clothing objects
clothes_rect_pos = [
    (20, 20, 72, 72), (102, 20, 72, 72),
    (184, 20, 72, 72), (266, 20, 72, 72),
    (20, 102, 72, 72), (102, 102, 72, 72),
    (184, 102, 72, 72), (266, 102, 72, 72)
]

# Define categories for clothing
categories = ['pants', 'pants', 'hat', 'hat', 'top', 'top', 'top', 'top']
clothes_prices = [5, 10, 15, 20, 5, 10, 15, 20]  # Prices for each item

# Create clothing objects
clothes_objects = [
    Clothing(f'clothing{i}', categories[i], (60, 48, 31), *pos, clothes_images[i],
             clothes_prices[i],
             HAT_SCALE if categories[i] == 'hat' else
             PANTS_SCALE if categories[i] == 'pants' else TOP_SCALE,
             (100, 100) if categories[i] == 'hat' else
             (50, 150) if categories[i] == 'pants' else
             (70, 120))  # Adjust position based on category
    for i, pos in enumerate(clothes_rect_pos)
]

# Initial state
coins = 100
selected_clothing = None  # Store the currently selected clothing item
equipped_clothing = {
    'pants': None,
    'hat': None,
    'top': None
}  # Store equipped clothing items from different categories

# Main loop
while True:
    mouse_pos = pygame.mouse.get_pos()  # Get current mouse position
    buy_button_enabled = selected_clothing and not selected_clothing.bought and coins >= selected_clothing.price
    equip_button_enabled = selected_clothing and selected_clothing.bought

    # Set button colors based on enabled/disabled state
    buy_button_color = (60, 48, 31) if buy_button_enabled else (100, 100, 100)
    equip_button_color = (60, 48, 31) if equip_button_enabled else (100, 100, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle clothing item selection
            for clothes in clothes_objects:
                if clothes.rect.collidepoint(mouse_pos):
                    selected_clothing = clothes  # Select the clothing item

            # Handle buy button click
            if buy_button_enabled and buy_button.collidepoint(mouse_pos):
                coins -= selected_clothing.price
                selected_clothing.bought = True

            # Handle equip button click
            if equip_button_enabled and equip_button.collidepoint(mouse_pos):
                equipped_clothing[selected_clothing.category] = selected_clothing.cat_image

    # Draw background
    screen.blit(background_surf, (0, 0))

    # Draw all clothing objects, with highlight if selected
    for clothes in clothes_objects:
        highlight = clothes == selected_clothing  # Highlight if selected
        clothes.draw(screen, highlight)

    # Draw the cat box
    cat_box = pygame.draw.rect(screen, (176, 135, 94), pygame.Rect(358, 20, 232, 360))

    # Draw Mike the cat
    screen.blit(mike_image, (cat_box.x + 45, cat_box.y + 20))

    # Draw equipped clothing on the cat
    if equipped_clothing['pants']:
        screen.blit(equipped_clothing['pants'], (cat_box.x + 57, cat_box.y + 150))  # Position for pants
    if equipped_clothing['hat']:
        screen.blit(equipped_clothing['hat'], (cat_box.x + 65, cat_box.y + -10))  # Position for hat
    if equipped_clothing['top']:
        screen.blit(equipped_clothing['top'], (cat_box.x + 38, cat_box.y + 72))  # Position for top

    # Draw price message if a clothing item is selected
    if selected_clothing:
        price_text = font.render(f"IT COSTS {selected_clothing.price} COINS", True, (255, 255, 255))
        screen.blit(price_text, (40, 300))  # Position the price text above buy and equip buttons

    # Draw Buy Button
    buy_button = pygame.draw.rect(screen, buy_button_color, pygame.Rect(40, 256, 119, 40))
    buy_text = font.render("Buy", True, (255, 255, 255))  # White text
    screen.blit(buy_text, (buy_button.x + 35, buy_button.y + 6))  # Centered

    # Change buy button color on hover
    if buy_button_enabled and buy_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (80, 80, 80), buy_button)  # Darker shade on hover
        screen.blit(buy_text, (buy_button.x + 35, buy_button.y + 6))

    # Draw Equip Button
    equip_button = pygame.draw.rect(screen, equip_button_color, pygame.Rect(189, 256, 119, 40))
    equip_text = font.render("Equip", True, (255, 255, 255))  # White text
    screen.blit(equip_text, (equip_button.x + 25, equip_button.y + 6))

    # Change equip button color on hover
    if equip_button_enabled and equip_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (80, 80, 80), equip_button)  # Darker shade on hover
        screen.blit(equip_text, (equip_button.x + 25, equip_button.y + 6))

    # Display coin count
    coin_text = font.render(f"Coins: {coins}", True, (255, 255, 0))  # Yellow text
    screen.blit(coin_text, (10, 350))

    # Update the display
    pygame.display.flip()
