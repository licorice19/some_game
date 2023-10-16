import pygame
from settings import GRID_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, CELL_SIZE

def handle_keyboard_events(cam_x, cam_y):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        cam_x -= 1
    if keys[pygame.K_RIGHT]:
        cam_x += 1
    if keys[pygame.K_UP]:
        cam_y -= 1
    if keys[pygame.K_DOWN]:
        cam_y += 1

    # Проверяем, чтобы камера не вышла за пределы поля
    cam_y = max(0, min(GRID_SIZE - SCREEN_WIDTH // CELL_SIZE, cam_y))
    cam_x = max(0, min(GRID_SIZE - SCREEN_HEIGHT // CELL_SIZE, cam_x))

    return cam_x, cam_y