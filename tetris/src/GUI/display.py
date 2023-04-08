import pygame
from time import sleep

def setup():
    caption = "Tetris"
    display_resolution = ((720, 720))

    display = pygame.display.set_mode(display_resolution)

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)

    return display, caption, display_resolution, font

def render(grid, score, display, disp_res, font):
  #sidebar
  pygame.draw.rect(display, (140, 176, 40), ((0,0),(disp_res[0]/3, disp_res[1])))
  display.blit(font.render(str(score), False, (0,0,0)), (disp_res[0]/6, disp_res[1]/5))

  #core tetris grid
  pygame.draw.rect(display, (255, 255, 255), ((disp_res[0]/3,0),(disp_res[0], disp_res[1])))
  grid_px_size = ((disp_res[1])/20)
  start_corner = (disp_res[0]/3,0)
  for square in grid:
    top_corner = (start_corner[0]+(square[1]*grid_px_size)+2, 
                  start_corner[1]+(square[2]*grid_px_size)+2)
    size = (grid_px_size-2, grid_px_size-2)
    if not square[0]:
      pygame.draw.rect(display, (0, 0, 0), (top_corner, size))

  return