import random

class CellMaterial:
    def __init__(self, name, base_color):
        self.name = name  # Название материала
        self.base_color = base_color  # Базовый цвет материала

materials = {
    "Water": CellMaterial("Water", (0, 165, 252)),
    "Stone": CellMaterial("Stone", (169, 169, 169)),
    "Dirt": CellMaterial("Dirt", (13, 166, 74)),
    "Sand": CellMaterial("Sand", (247, 243, 12)),
    "Deep Water": CellMaterial("Deep Water", (0, 20, 138)),
    "Snow": CellMaterial("Snow", (254, 254, 254)),
}
