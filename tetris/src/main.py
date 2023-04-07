import pygame
from GUI import display, interaction
from model import tetris_grid

def main():
    # Standard board 10 wide 20 tall
    # board settings, will be refactored
    
    dp, cap, resolution = display.setup()
    pygame.display.set_caption(cap)
    pygame.init()

    grid = tetris_grid.Grid()
    grid.update_grid(2,3, True)
    grid.update_grid(5,7, True)
    grid.update_grid(9,15, True)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display.render(grid, dp, resolution)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
