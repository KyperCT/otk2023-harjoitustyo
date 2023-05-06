import pygame


def get_keypresses() -> tuple:
    """Gets relevant keypresses from pygame

    Returns:
      tuple(bool) with inputs in order up, left, right, down
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


def exit_program() -> bool:
    """Returns if escape key is pressed

    Returns:
      True if pressed, False if not
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        return True
    return False


def update_keypresses(keys) -> tuple:
    current_keys = get_keypresses()
    new_presses = list(keys)
    for i in range(0, len(current_keys)):
        if current_keys[i]:
            new_presses[i] = True
    return tuple(new_presses)


def any_key() -> bool:
    """Returns if any key is pressed

    Returns:
      True if pressed, False if not
    """
    keys = pygame.key.get_pressed()
    if True in keys:
        return True
    return False

def collect_keypress_text(events) -> tuple:
    """Gets user text input for score entry

    Returns:
      Returns one of three tuples (0, "") for enter, (1, "") for backspace (2, str) for text
    """
    output = ""
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return 0, ""
            if event.key == pygame.K_BACKSPACE:
                return 1, ""
            output += event.unicode
    return 2, output
