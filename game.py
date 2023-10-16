import pygame
import world
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, CELL_SIZE
from keyboard import handle_keyboard_events
from debug import print_selected_material

clock = pygame.time.Clock()

cam_x, cam_y = 0,0
def handle_events():
    global cam_x, cam_y
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print_selected_material(world.grid, cam_x, cam_y)
        if keys[pygame.K_LEFT]:
            cam_x -= 3
        if keys[pygame.K_RIGHT]:
            cam_x += 3
        if keys[pygame.K_UP]:
            cam_y -= 3
        if keys[pygame.K_DOWN]:
            cam_y += 3
    return True

def draw_grid(screen, camera_x, camera_y):
    for x in range(max(0, camera_x), min(camera_x + SCREEN_WIDTH // CELL_SIZE, GRID_SIZE)):
        for y in range(max(0, camera_y), min(camera_y + SCREEN_HEIGHT // CELL_SIZE, GRID_SIZE)):
            world.grid[x][y].draw(screen, x - camera_x, y - camera_y)


def Game():
    global cam_x, cam_y
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        running = handle_events()
        cam_x, cam_y = handle_keyboard_events(cam_x, cam_y)
        screen.fill((0, 0, 0))
        draw_grid(screen, cam_x, cam_y)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()