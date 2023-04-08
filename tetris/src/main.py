import pygame
from GUI import display, interaction
from model import tetris_grid
from logic import movement

def main():
    # Standard board 10 wide 20 tall
    # board settings, will be refactored
    
    dp, cap, resolution = display.setup()
    pygame.display.set_caption(cap)
    clock = pygame.time.Clock()
    pygame.init()

    grid = tetris_grid.Grid()

    running = True
    frame = 0
    tick_speed = 10

    blocks = []
    state = 0

    while running:
        frame = (frame+1)%(tick_speed/4)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = interaction.get_keypresses()
        state = movement.main_move(grid, keys, blocks, state)
        display.render(grid, dp, resolution)
        pygame.display.update()
        clock.tick(tick_speed)


    pygame.quit()


if __name__ == "__main__":
    main()
