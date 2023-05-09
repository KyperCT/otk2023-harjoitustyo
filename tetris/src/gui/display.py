import pygame


def setup():
    """Defines and generates basic UI elements.

    Returns: Pygame display, window caption, Resolution, font
    """
    caption = "Tetris"
    display_resolution = (720, 720)

    display = pygame.display.set_mode(display_resolution)

    pygame.font.init()
    font = pygame.font.SysFont("monospace", 30, bold=True)

    return display, caption, display_resolution, font


def render(grid, score, display, disp_res, font):
    """Renders game elements

    Args:
      grid: tetris grid
      score: score value
      display: pygame display
      disp_res: display resolution
      font: font for text elements
    """
    # sidebar
    pygame.draw.rect(display, (140, 176, 40), ((0, 0), (disp_res[0] / 3, disp_res[1])))
    display.blit(
        font.render(str(score), False, (0, 0, 0)), (disp_res[0] / 6, disp_res[1] / 5)
    )

    # core tetris grid
    pygame.draw.rect(
        display, (255, 255, 255), ((disp_res[0] / 3, 0), (disp_res[0], disp_res[1]))
    )
    grid_px_size = (disp_res[1]) / 20
    start_corner = (disp_res[0] / 3, 0)
    for square in grid:
        top_corner = (
            start_corner[0] + (square[1] * grid_px_size) + 2,
            start_corner[1] + (square[2] * grid_px_size) + 2,
        )
        size = (grid_px_size - 2, grid_px_size - 2)
        if not square[0]:
            pygame.draw.rect(display, (0, 0, 0), (top_corner, size))


def menu_screen(high_score_list, display, disp_res, font):
    """Renders menu screen displayed between games
    Args:
      high_score_list: ordered list of high scores
      display: pygame display
      disp_res: display resolution
      font: font for text elements
    """
    pygame.draw.rect(
        display,
        (140, 176, 40),
        ((0, 0), (disp_res[0], disp_res[1])),
    )
    visual_row = 0
    for data in high_score_list:
        display.blit(
            font.render(f"{data[0]:<14}{data[1]}", False, (0, 0, 0)),
            (disp_res[0] / 4, (disp_res[1] / 8) + (32 * visual_row)),
        )
        visual_row += 1
    display.blit(
        font.render(str("Press any key to start"), False, (0, 0, 0)),
        (disp_res[0] / 3, (disp_res[1] / 8) + (32 * visual_row)),
    )
    visual_row += 1
    display.blit(
        font.render(str("Press ESC to exit"), False, (0, 0, 0)),
        (disp_res[0] / 3, (disp_res[1] / 8) + (32 * visual_row)),
    )


def score_name_entry(score, text, display, disp_res, font):
    """Renders box for name entry
    Args:
      score: total score from game
      text: text given as name
      display: pygame display
      disp_res: display resolution
      font: font for text elements
    """
    pygame.draw.rect(
        display,
        (130, 174, 40),
        ((disp_res[0] / 4, disp_res[0] / 3), (disp_res[0] / 2, disp_res[0] / 4)),
    )
    display.blit(
        font.render(str(score), False, (0, 0, 0)),
        (disp_res[0] / 2, disp_res[0] / 4 + disp_res[0] / 8),
    )
    display.blit(
        font.render(str("Enter Name:"), False, (0, 0, 0)),
        (disp_res[0] / 3, disp_res[0] / 4 + (disp_res[0] / 8) * (1.5)),
    )
    pygame.draw.rect(
        display,
        (110, 154, 20),
        (
            (disp_res[0] / 3, disp_res[0] / 4 + (disp_res[0] / 8) * 2),
            (disp_res[0] / 5, 40),
        ),
    )
    display.blit(
        font.render(str(text), False, (0, 0, 0)),
        (disp_res[0] / 3, disp_res[0] / 4 + (disp_res[0] / 8) * 2),
    )
