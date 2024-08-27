import pygame
from sys import exit
from game import game_loop  # Import the game loop function

# Initialize Pygame
pygame.init()
pygame.mixer.init()



# Set up the display
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w, display_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Set up fonts and other global resources
font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 50)
test_font = pygame.font.Font(None, 50)

# Colors
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

pygame.mixer.music.load('./Starlit Dreams.mp3')
pygame.mixer.music.set_volume(0.2)



# Menu options
menu_options = ["Start Game", "Options", "Quit"]
selected_option = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def main_menu():
    global selected_option

    while True:
        pygame.mixer.music.play(-1)
        screen.fill((0, 0, 0))

        # Get the mouse position and clicks
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Display the menu options
        for i, option in enumerate(menu_options):
            color = PINK if i == selected_option else WHITE
            draw_text(option, font, color, screen, screen_width / 2, screen_height / 2 - 100 + i * 150)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                if event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        # Pass the necessary parameters to game_loop
                        game_loop(screen, screen_width, screen_height, test_font)
                    elif selected_option == 1:
                        # Placeholder for Options, implement as needed
                        draw_text("Options - Not Implemented", small_font, WHITE, screen, screen_width / 2, screen_height / 2 + 200)
                        pygame.display.update()
                        pygame.time.wait(2000)
                    elif selected_option == 2:
                        pygame.quit()
                        exit()

            if event.type == pygame.MOUSEMOTION:
                for i, option in enumerate(menu_options):
                    option_rect = pygame.Rect(screen_width / 2 - 200, screen_height / 2 - 100 + i * 150 - 50, 400, 100)
                    if option_rect.collidepoint(mouse_pos):
                        selected_option = i

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_click[0]:
                    if selected_option == 0:
                        # Pass the necessary parameters to game_loop
                        game_loop(screen, screen_width, screen_height, test_font)
                    elif selected_option == 1:
                        # Placeholder for Options, implement as needed
                        draw_text("Options - Not Implemented", small_font, WHITE, screen, screen_width / 2, screen_height / 2 + 200)
                        pygame.display.update()
                        pygame.time.wait(2000)
                    elif selected_option == 2:
                        pygame.quit()
                        exit()

        pygame.display.update()

# Main execution block
if __name__ == "__main__":
    main_menu()  # Display the main menu first
