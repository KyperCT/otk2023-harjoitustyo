import pygame
from GUI import display, interaction
from model import tetris_grid, tetris_block
from logic import movement, score

def main():
    '''
    Main loop for tetris game. Runs initialization functions, and then runs the core game functions in a loop.
    Ensures operations are done on appropriate frames.
    '''
    
    dp, cap, resolution, font = display.setup()
    pygame.display.set_caption(cap)
    clock = pygame.time.Clock()
    pygame.init()

    grid = tetris_grid.Grid()

    running = True
    tick_speed = 10
    game_speed = 4
    state = 0

    blocks = [tetris_block.Block()]
    total_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if len(blocks) == 0:
            blocks.append(tetris_block.Block())
            movement.grid_update(grid, blocks)
        else:
            keys = interaction.get_keypresses()
            movement.user_move(grid, keys, blocks)
            if state == game_speed:
                movement.game_move(grid, blocks)
                state = 0
            else:
                state += 1
        if len(blocks) == 0:
            display.render(grid, total_score, dp, resolution, font)
            pygame.display.update()
            pygame.time.wait(250)
            total_score = score.check_score(grid, total_score)
        display.render(grid, total_score, dp, resolution, font)
        pygame.display.update()
        clock.tick(tick_speed)


    pygame.quit()


if __name__ == "__main__":
    main()
