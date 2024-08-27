

    if is_jumping:
        y_pos += jump_velocity  # Move character based on jump velocity
        jump_velocity += 1  # Apply gravity

        # Check if character has landed back on the ground
        if y_pos >= screen_height - 100:
            y_pos = screen_height - 100  # Reset position to ground level
            is_jumping = False  # End the jump

    # Prevent the character from moving off the screen
    if x_pos < 0:
        x_pos = 0
    elif x_pos > screen_width - 100:  # Assuming character width is 100 pixels
        x_pos = screen_width - 100

    # Select the appropriate animation frame
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
