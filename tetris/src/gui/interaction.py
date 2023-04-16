import pygame


def get_keypresses() -> tuple:
    """
    output: tuple(bool) with inputs in order up, left, right, down
    """
    keys = pygame.key.get_pressed()
    up_direction, left, right, down = False, False, False, False
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        up_direction = True
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        left = True
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        right = True
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        down = True
    return up_direction, left, right, down


def update_keypresses(keys) -> tuple:
    current_keys = get_keypresses()
    new_presses = list(keys)
    for i in range(0, len(current_keys)):
        if current_keys[i]:
            new_presses[i] = True
    return tuple(new_presses)
