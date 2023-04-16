import pygame
from gui import display, interaction
from model import tetris_grid
from logic import core


def main():
    # Standard board 10 wide 20 tall
    # board settings, will be refactored

    main_display, cap, resolution, font = display.setup()
    pygame.display.set_caption(cap)
    clock = pygame.time.Clock()
    pygame.init()

    grid = tetris_grid.Grid()
    total_score = 0

    running = True
    tick_speed = 10
    state = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if interaction.exit():
            running = False
        keys = interaction.get_keypresses()
        grid, total_score, state = core.core_loop(grid, total_score, keys, state)
        display.render(grid, total_score, main_display, resolution, font)
        pygame.display.update()
        clock.tick(tick_speed)

    pygame.quit()


if __name__ == "__main__":
    main()
