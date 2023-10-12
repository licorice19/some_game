import pygame
import world
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, CELL_SIZE
from keyboard import move_camera
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
            print_selected_material(world.grid)
        if keys[pygame.K_LEFT]:
            cam_x -= 1
        if keys[pygame.K_RIGHT]:
            cam_x += 1
        if keys[pygame.K_UP]:
            cam_y -= 1
        if keys[pygame.K_DOWN]:
            cam_y += 1
    return True

def draw_grid(screen, camera_x, camera_y):
        for x in range(camera_x, min(camera_x + SCREEN_WIDTH // CELL_SIZE, GRID_SIZE)):
            for y in range(camera_y, min(camera_y + SCREEN_HEIGHT // CELL_SIZE, GRID_SIZE)):
                world.grid[x][y].draw(screen)

def Game():
    global cam_x, cam_y
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        running = handle_events()

        screen.fill((0, 0, 0))
        draw_grid(screen, cam_x, cam_y)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()