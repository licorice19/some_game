from settings import GRID_SIZE
from mouse import get_clicked_square
import pygame

def print_selected_material(grid, camera_x, camera_y):
    clicked_square = get_clicked_square(camera_x, camera_y)
    x, y = clicked_square
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        selected_cell = grid[x][y]
        print(f"Название материала: {selected_cell.material[0].name}")
