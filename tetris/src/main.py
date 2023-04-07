import pygame


def main():
    # Standard board 10 wide 20 tall
    # board settings, will be refactored
    tetris_grid = (10, 20)
    sidebar = (10, 20)
    border = 2

    grid_square_size = 20
    display_resolution = (grid_square_size*(tetris_grid[0]+sidebar[0]+border*2), grid_square_size*(tetris_grid[1]+border*2))

    display = pygame.display.set_mode(display_resolution)
    pygame.display.set_caption("Tetris")
    pygame.init()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.draw.rect(display, (140, 176, 40), ((border*grid_square_size,border*grid_square_size),(grid_square_size*sidebar[0],grid_square_size*sidebar[1])))

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
