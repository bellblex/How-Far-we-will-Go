import pygame
from sys import exit
from movement import move_and_render_character 

pygame.init()

# Set up the display
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

# Load Girl Walk Right
surface_girl_right = []
for i in range(1, 21):
    image = pygame.image.load(f'./png/Run ({i}).png').convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    surface_girl_right.append(image)

# Load Girl Walk Left 
surface_girl_left = []
for image in surface_girl_right:
    flipped_image = pygame.transform.flip(image, True, False)  # Flip horizontally
    surface_girl_left.append(flipped_image)

# Load Girl Jump Right
surface_girl_jump_right = []
for i in range(1, 31):
    image = pygame.image.load(f'./png/Jump ({i}).png').convert_alpha()
    image = pygame.transform.scale(image, (100, 100))
    surface_girl_jump_right.append(image)

# Load Girl Jump Left
surface_girl_jump_left = []
for image in surface_girl_jump_right:
    flipped_image = pygame.transform.flip(image, True, False)  # Flip horizontally
    surface_girl_jump_left.append(flipped_image)

# Load Boy Walk Right
surface_boy_right = []
for i in range(1, 16):
    image = pygame.image.load(f'./png/flatboy/png/Run ({i}).png').convert_alpha()
    image = pygame.transform.scale(image, (150, 150))
    surface_boy_right.append(image)

# Load Boy Walk Left 
surface_boy_left = []
for image in surface_boy_right:
    flipped_image = pygame.transform.flip(image, True, False)  # Flip horizontally
    surface_boy_left.append(flipped_image)

# Load Boy Jump Right
surface_boy_jump_right = []
for i in range(1, 16):
    image = pygame.image.load(f'./png/flatboy/png/Jump ({i}).png').convert_alpha()
    image = pygame.transform.scale(image, (150, 150))
    surface_boy_jump_right.append(image)

# Load Boy Jump Left
surface_boy_jump_left = []
for image in surface_boy_jump_right:
    flipped_image = pygame.transform.flip(image, True, False)  # Flip horizontally
    surface_boy_jump_left.append(flipped_image)

# Load backgrounds 
surface_skye1 = pygame.image.load('./free-sky-with-clouds-background-pixel-art-set/Clouds/Clouds 2/1.png').convert_alpha()
surface_skye1 = pygame.transform.scale(surface_skye1, (screen_width, screen_height))

surface_skye2 = pygame.image.load('./free-sky-with-clouds-background-pixel-art-set/Clouds/Clouds 2/2.png').convert_alpha()
surface_skye2 = pygame.transform.scale(surface_skye2, (screen_width, screen_height))

surface_skye3 = pygame.image.load('./free-sky-with-clouds-background-pixel-art-set/Clouds/Clouds 2/3.png').convert_alpha()
surface_skye3 = pygame.transform.scale(surface_skye3, (screen_width, screen_height))

surface_skye4 = pygame.image.load('./free-sky-with-clouds-background-pixel-art-set/Clouds/Clouds 2/4.png').convert_alpha()
surface_skye4 = pygame.transform.scale(surface_skye4, (screen_width, screen_height))

# Scrolling
background_x1 = 0
background_x2 = screen_width
scroll_speed = 3 
# Text
surface_text = test_font.render('GoncaDu', False, 'Pink')
text_rect = surface_text.get_rect(center=(screen_width / 2, screen_height / 2))

# Player's starting position, animation index, and direction
girl_x_pos = screen_width / 2 - 50  
girl_y_pos = screen_height - 100  
girl_index = 0
moving_right = True  
is_jumping = False
jump_velocity = 0


boy_x_pos = screen_width / 2 - 50 
boy_y_pos = screen_height - 100  
boy_index = 0
boy_moving_right = True  
boy_is_jumping = False
boy_jump_velocity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    background_x1 -= scroll_speed
    background_x2 -= scroll_speed

    
    if background_x1 <= -screen_width:
        background_x1 = screen_width
    if background_x2 <= -screen_width:
        background_x2 = screen_width

  
    screen.blit(surface_skye1, (background_x1, 0))
    screen.blit(surface_skye1, (background_x2, 0))
    screen.blit(surface_skye2, (background_x1, 0))
    screen.blit(surface_skye2, (background_x2, 0))
    screen.blit(surface_skye3, (background_x1, 0))
    screen.blit(surface_skye3, (background_x2, 0))
    screen.blit(surface_skye4, (background_x1, 0))
    screen.blit(surface_skye4, (background_x2, 0))
    
    # Defined girl
    girl_x_pos, girl_y_pos, moving_right, is_jumping, jump_velocity = move_and_render_character(
        'player1', girl_x_pos, girl_y_pos,
        surface_girl_right, surface_girl_left,
        surface_girl_jump_right, surface_girl_jump_left,
        moving_right, is_jumping, jump_velocity,
        screen_width, screen_height,
        screen, girl_index
    )

    # Defined boy
    boy_x_pos, boy_y_pos, boy_moving_right, boy_is_jumping, boy_jump_velocity = move_and_render_character(
        'player2', boy_x_pos, boy_y_pos,
        surface_boy_right, surface_boy_left,
        surface_boy_jump_right, surface_boy_jump_left,
        boy_moving_right, boy_is_jumping, boy_jump_velocity,
        screen_width, screen_height,
        screen, boy_index
    )
    # Update animation frame
    girl_index = (girl_index + 1) % len(surface_girl_right)
    boy_index = (boy_index + 1) % len(surface_boy_right)

    screen.blit(surface_text, text_rect.topleft)

    pygame.display.update()
    clock.tick(15)
