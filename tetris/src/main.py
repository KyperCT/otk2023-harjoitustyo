import pygame


def main():
    # Standard board 10 wide 20 tall
    pygame.display.set_mode((720, 720))
    pygame.display.set_caption("Tetris")
    pygame.init()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
