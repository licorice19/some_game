import pygame
from settings import CELL_SIZE

def get_clicked_square():
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos
    x //= CELL_SIZE
    y //= CELL_SIZE
    return x, y