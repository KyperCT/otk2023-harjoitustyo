import pygame
from gui import display, interaction
from model import tetris_grid
from logic import core
from database import db_interact


def main():
    """
    Main loop for tetris game. Runs initialization functions, 
    and then runs the core game functions in a loop.
    Ensures operations are done on appropriate frames.
    """

    main_display, cap, resolution, font = display.setup()

    pygame.display.set_caption(cap)
    clock = pygame.time.Clock()
    pygame.init()

    grid = tetris_grid.Grid()
    total_score = 0
    db_interact.database_startup()

    running = True
    tick_speed = 10
    state = None
    in_menu = True
    in_fail = False
    in_game = False
    eventlist = []
    username = ""

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            eventlist.append(event)

        if interaction.exit_program():
            running = False
        if in_menu:
            score_list = db_interact.database_get_top_scores()
            display.menu_screen(score_list, main_display, resolution, font)
            if interaction.any_key():
                in_menu = False
                in_game = True
        if in_fail:
            keytype, text = interaction.collect_keypress_text(eventlist)
            username += text
            if keytype == 1:
                username = username[:-1]
            display.score_name_entry(
                total_score, username, main_display, resolution, font
            )
            if keytype == 0:
                db_interact.database_enter_new_score(username, total_score)
                state = None
                grid.clear()
                in_menu = True
                in_fail = False
                username = ""
                total_score = 0
        if in_game:
            keys = interaction.get_keypresses()
            grid, total_score, state = core.core_loop(grid, total_score, keys, state)
            display.render(grid, total_score, main_display, resolution, font)
            if state["fail"]:
                in_fail = True
                in_game = False

        pygame.display.update()
        clock.tick(tick_speed)
        eventlist = []

    pygame.quit()


if __name__ == "__main__":
    main()
