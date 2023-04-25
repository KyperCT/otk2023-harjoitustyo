import pygame
from gui import display, interaction
from model import tetris_grid
from logic import core


def main():
    '''
    Main loop for tetris game. Runs initialization functions, and then runs the core game functions in a loop.
    Ensures operations are done on appropriate frames.
    '''

    main_display, cap, resolution, font = display.setup()

    pygame.display.set_caption(cap)
    clock = pygame.time.Clock()
    pygame.init()

    grid = tetris_grid.Grid()
    total_score = 0

    running = True
    tick_speed = 10
    state = None
    in_menu = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if interaction.exit():
            running = False
        if in_menu:
            display.menu_screen(main_display, resolution, font)
            if interaction.any_key():
                in_menu = False
            else:
                pygame.display.update()
                continue
        keys = interaction.get_keypresses()
        grid, total_score, state = core.core_loop(grid, total_score, keys, state)
        display.render(grid, total_score, main_display, resolution, font)
        pygame.display.update()
        clock.tick(tick_speed)
        if state["fail"]:
            in_menu = True
            state = None
            grid.clear()

    pygame.quit()


if __name__ == "__main__":
    main()
