import pygame
from sys import exit
from movement import move_and_render_character 
from interaction import help_love

def game_loop(screen, screen_width, screen_height, test_font):
    clock = pygame.time.Clock()

    # Load Girl Walk Right
    surface_girl_right = []
    for i in range(1, 21):
        image = pygame.image.load(f'./png/Run ({i}).png').convert_alpha()
        image = pygame.transform.scale(image, (100, 100))
        surface_girl_right.append(image)

    # Load Girl Walk Left 
    surface_girl_left = []
    for image in surface_girl_right:
        flipped_image = pygame.transform.flip(image, True, False) 
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
        flipped_image = pygame.transform.flip(image, True, False)  
        surface_girl_jump_left.append(flipped_image)
        
    # Load Girl Idle Right
    surface_girl_idle_right = []
    for i in range(1, 17):  # 16 idle frames
        image = pygame.image.load(f'./png/Idle ({i}).png').convert_alpha()
        image = pygame.transform.scale(image, (100, 100))
        surface_girl_idle_right.append(image)

    # Load Girl Idle Left
    surface_girl_idle_left = []
    for image in surface_girl_idle_right:
        flipped_image = pygame.transform.flip(image, True, False)  
        surface_girl_idle_left.append(flipped_image)

    # Load Boy Walk Right
    surface_boy_right = []
    for i in range(1, 16):
        image = pygame.image.load(f'./png/flatboy/png/Run ({i}).png').convert_alpha()
        image = pygame.transform.scale(image, (135, 135))
        surface_boy_right.append(image)

    # Load Boy Walk Left 
    surface_boy_left = []
    for image in surface_boy_right:
        flipped_image = pygame.transform.flip(image, True, False)  
        surface_boy_left.append(flipped_image)

    # Load Boy Jump Right
    surface_boy_jump_right = []
    for i in range(1, 16):
        image = pygame.image.load(f'./png/flatboy/png/Jump ({i}).png').convert_alpha()
        image = pygame.transform.scale(image, (135, 135))
        surface_boy_jump_right.append(image)

    # Load Boy Jump Left
    surface_boy_jump_left = []
    for image in surface_boy_jump_right:
        flipped_image = pygame.transform.flip(image, True, False)  
        surface_boy_jump_left.append(flipped_image)

    # Load Boy Idle Right
    surface_boy_idle_right = []
    for i in range(1, 16):  
        image = pygame.image.load(f'./png/flatboy/png/Idle ({i}).png').convert_alpha()
        image = pygame.transform.scale(image, (135, 135))
        surface_boy_idle_right.append(image)

    # Load Boy Idle Left
    surface_boy_idle_left = []
    for image in surface_boy_idle_right:
        flipped_image = pygame.transform.flip(image, True, False) 
        surface_boy_idle_left.append(flipped_image)
        
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
    ground_height = 100
    ground_x1 = 0
    ground_x2 = screen_width
    scroll_speed = 3
    ground_color = (34, 139, 34)

    # Text
    surface_text = test_font.render('How Far We Will Go', False, 'Pink')
    text_rect = surface_text.get_rect(center=(screen_width / 2, screen_height / 2))

    # Player's starting position, animation index, and movement variables
    # Initialize girl character variables
    girl_x_pos = 100
    girl_y_pos = screen_height - ground_height - 100 
    girl_index = 0
    moving_right = True
    is_jumping = False
    jump_velocity = 0

    # Initialize boy character variables
    boy_x_pos = screen_width - 200
    boy_y_pos = screen_height - ground_height - 120
    boy_index = 0
    boy_moving_right = True
    boy_is_jumping = False
    boy_jump_velocity = 0


    player1_width = 100  
    player1_height = 100  
    player2_width = 135  
    player2_height = 135 

    girl_ability_used = False
    boy_ability_used = False
    girl_ability_activated = False
    boy_ability_activated = False

    # Item properties
    girl_item_x, girl_item_y = girl_x_pos + 50, girl_y_pos
    boy_item_x, boy_item_y = boy_x_pos - 50, boy_y_pos
    item_speed = 10
    girl_item_angle = 0
    boy_item_angle = 0

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
        
        # Draw the ground
        pygame.draw.rect(screen, ground_color, (ground_x1, screen_height - ground_height, screen_width, ground_height))
        pygame.draw.rect(screen, ground_color, (ground_x2, screen_height - ground_height, screen_width, ground_height))

        # Add some details to the ground (e.g., lines, circles, etc.)
        for i in range(ground_x1, ground_x1 + screen_width, 50):
            pygame.draw.line(screen, (0, 100, 0), (i, screen_height - ground_height), (i + 25, screen_height - ground_height + 25), 3)
            for i in range(ground_x2, ground_x2 + screen_width, 50):
                pygame.draw.line(screen, (0, 100, 0), (i, screen_height - ground_height), (i + 25, screen_height - ground_height + 25), 3)

        girl_x_pos, girl_y_pos, moving_right, is_jumping, jump_velocity = move_and_render_character(
        'player1', girl_x_pos, girl_y_pos,
        surface_girl_right, surface_girl_left,
        surface_girl_jump_right, surface_girl_jump_left,
        surface_girl_idle_right, surface_girl_idle_left,
        moving_right, is_jumping, jump_velocity,
        screen_width, screen_height, ground_height, screen, girl_index
    )

        boy_x_pos, boy_y_pos, boy_moving_right, boy_is_jumping, boy_jump_velocity = move_and_render_character(
       'player2', boy_x_pos, boy_y_pos,
       surface_boy_right, surface_boy_left,
       surface_boy_jump_right, surface_boy_jump_left,
       surface_boy_idle_right, surface_boy_idle_left,
       boy_moving_right, boy_is_jumping, boy_jump_velocity,
       screen_width, screen_height, ground_height, screen, boy_index  
    )
        
        if not girl_ability_used:
            girl_item_x, girl_item_y, girl_item_angle, girl_ability_used, girl_ability_activated = help_love(
                'player1', girl_item_x, girl_item_y, item_speed, girl_item_angle,
                screen, girl_x_pos, girl_y_pos, player1_width, player1_height, boy_x_pos, boy_y_pos, girl_ability_activated, screen_width
            )

        if not boy_ability_used:
            boy_item_x, boy_item_y, boy_item_angle, boy_ability_used, boy_ability_activated = help_love(
                'player2', boy_item_x, boy_item_y, item_speed, boy_item_angle,
                screen, boy_x_pos, boy_y_pos, player2_width, player2_height, girl_x_pos, girl_y_pos, boy_ability_activated, screen_width
            )

        # Update animation frame
        girl_index = (girl_index + 1) % len(surface_girl_right)
        boy_index = (boy_index + 1) % len(surface_boy_right)

        screen.blit(surface_text, text_rect.topleft)

        pygame.display.update()
        clock.tick(15)
