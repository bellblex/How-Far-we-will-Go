import pygame

def help_love(player, item_x, item_y, item_speed, item_angle, screen, player_x, player_y, player_width, player_height, target_x, target_y, ability_activated, screen_width):
    def get_controls():
        if player == 'player1':  
            return pygame.K_KP1  
        elif player == 'player2':  
            return pygame.K_1  

    ability_1 = get_controls()
    
    if ability_1 is None:
        return item_x, item_y, item_angle, False, ability_activated
    
    keys = pygame.key.get_pressed()

    if keys[ability_1] and not ability_activated:
        ability_activated = True
        item_x = player_x + player_width // 2 
        item_y = player_y + player_height // 2  

    if ability_activated:
        item_angle += 10
        item_bigger = pygame.transform.scale(pygame.image.load('Health potion.png').convert_alpha(), (50, 50))
        rotated_item = pygame.transform.rotate(item_bigger, item_angle)

        if player == 'player1':
            item_x += item_speed  
        elif player == 'player2':
            item_x -= item_speed  

        rotated_rect = rotated_item.get_rect(center=(item_x, item_y))

        screen.blit(rotated_item, rotated_rect.topleft)

        if (player == 'player1' and item_x >= target_x) or (player == 'player2' and item_x <= target_x):
            print(f"{player} has hit the target!")
            return item_x, item_y, item_angle, True, False  

        if (item_x > screen_width and player == 'player1') or (item_x < 0 and player == 'player2'):
            return item_x, item_y, item_angle, True, False
        
    return item_x, item_y, item_angle, False, ability_activated
