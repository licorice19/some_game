import pygame
import random
import noise
from settings import WHITE, CELL_SIZE, GRID_SIZE
from materials import materials, CellMaterial


def choose_material(x, y, scale, material_list):
    value = noise.pnoise2(
        x / scale,
        y / scale,
        octaves=2,
        persistence=0.5,
        lacunarity=5,
        repeatx=50,
        repeaty=50,
        base=0,
    )
    if -1 <= value <= -0.3:
        return material_list[4]
    if -0.3 <= value <= -0.2:
        return material_list[0]
    if -0.2 <= value <= -0.15:
        return material_list[3]
    elif -0.15 < value <= 0.4:
        return material_list[2]
    elif 0.4 < value <= 0.57:
        return material_list[1]
    elif 0.57 < value <= 1:
        return material_list[5]
    else:
        return material_list[0]


def generate_grid(material_list, scale=100):
    grid = [
        [
            Cell(x, y, choose_material(x, y, scale, material_list))
            for y in range(GRID_SIZE)
        ]
        for x in range(GRID_SIZE)
    ]
    return grid


class Cell:
    def __init__(self, x, y, material_name):
        self.x = x
        self.y = y
        self.material = materials.get(
            material_name, CellMaterial("По умолчанию", (0, 0, 0))
        )  # По умолчанию

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.material.color,  # Используйте self.material.color
            (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )


grid = generate_grid(list(materials.keys()), scale=30)
