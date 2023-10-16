import pygame
from settings import CELL_SIZE

def get_clicked_square(camera_x, camera_y):
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    x //= CELL_SIZE
    y //= CELL_SIZE
    x += camera_x
    y += camera_y
    return x, y