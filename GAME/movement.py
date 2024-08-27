import pygame

# Function to handle character movement and rendering
def move_and_render_character(player, x_pos, y_pos, surface_right, surface_left, surface_jump_right, surface_jump_left, moving_right, is_jumping, jump_velocity, screen_width, screen_height, screen, index):
    
    # Inner function to check which player is being controlled
    def get_controls():
        if player == 'player1':  
            return pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP
        elif player == 'player2':  
            return pygame.K_d, pygame.K_a, pygame.K_w
    
    right_key, left_key, jump_key = get_controls()

    keys = pygame.key.get_pressed()

    if keys[right_key]:
        x_pos += 10  
        moving_right = True
    elif keys[left_key]:
        x_pos -= 10  
        moving_right = False

    if not is_jumping:
        if keys[jump_key]:
            is_jumping = True
            jump_velocity = -15  

    if is_jumping:
        y_pos += jump_velocity  
        jump_velocity += 1 

        if y_pos >= screen_height - 100:
            y_pos = screen_height - 100  
            is_jumping = False  

    if x_pos < 0:
        x_pos = 0
    elif x_pos > screen_width - 100:  
        x_pos = screen_width - 100

    if is_jumping:
        if moving_right:
            screen.blit(surface_jump_right[index % len(surface_jump_right)], (x_pos, y_pos))
        else:
            screen.blit(surface_jump_left[index % len(surface_jump_left)], (x_pos, y_pos))
    else:
        if moving_right:
            screen.blit(surface_right[index % len(surface_right)], (x_pos, y_pos))
        else:
            screen.blit(surface_left[index % len(surface_left)], (x_pos, y_pos))

    return x_pos, y_pos, moving_right, is_jumping, jump_velocity
