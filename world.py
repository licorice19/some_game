import pygame
import random
import noise
from settings import CELL_SIZE, GRID_SIZE
from materials import materials, CellMaterial


def color_deviation(material, deviation=5):
    # Генерация случайных отклонений для каждой компоненты цвета
    
    red_deviation = random.randint(-deviation, deviation)
    green_deviation = random.randint(-deviation, deviation)
    blue_deviation = random.randint(-deviation, deviation)

    # Применение отклонений к базовому цвету
    color = (
        max(0, min(255, material.base_color[0] + red_deviation)),
        max(0, min(255, material.base_color[1] + green_deviation)),
        max(0, min(255, material.base_color[2] + blue_deviation)),
    )
    return material, color

def choose_material(x, y, scale, material_list):
    value = noise.pnoise2(
        x / scale,
        y / scale,
        octaves=2,
        persistence=0.8,
        lacunarity=5,
        repeatx=50,
        repeaty=50,
        base=0,
    )
    default = CellMaterial("По умолчанию", (0, 0, 0))
    if -1 <= value <= -0.2:
        return materials.get(material_list[4], default)
    elif -0.2 <= value <= -0.1:
        return  materials.get(material_list[0], default)
    elif -0.1 <= value <= -0:
        return  materials.get(material_list[3], default)
    elif -0 < value <= 0.1:
        return  materials.get(material_list[2], default)
    elif 0.1 < value <= 0.3:
        return  materials.get(material_list[1], default)
    elif 0.3 < value <= 1:
        return  materials.get(material_list[5], default)
    else:
        return  materials.get(material_list[0], default)


def generate_grid(material, scale=100):
    
    grid = [
        [
            Cell(x, y, color_deviation(choose_material(x, y, scale, material)))
            for y in range(GRID_SIZE)
        ]
        for x in range(GRID_SIZE)
    ]
    return grid


class Cell:
    def __init__(self, x, y, material):
        self.x = x
        self.y = y
        self.material = material

    def draw(self, screen, relative_x, relative_y):
        pygame.draw.rect(
            screen,
            self.material[1],  # Используйте self.material.base_color
            (relative_x * CELL_SIZE, relative_y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )

material_list = list(materials)
grid = generate_grid(material_list, scale=80)
