import pygame
import sys

pygame.init()
screen_width = 768
screen_height = 448
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
white = (255, 255, 255)

bg_surface = pygame.image.load('country-platform-files/country-platform-files/layers/country-platform-back.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

forest_surface = pygame.image.load('country-platform-files/country-platform-files/layers/forest_transp.png').convert_alpha()
forest_surface = pygame.transform.scale2x(forest_surface)
forest_surface_x = 0

floor_surface = pygame.image.load('country-platform-files/country-platform-files/layers/country-platform-tiles-example.png').convert_alpha()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_surface_x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    forest_surface_x -= 0.2
    if forest_surface_x <= -screen_width:
        forest_surface_x = 0
    floor_surface_x -= 1
    if floor_surface_x <= -screen_width:
        floor_surface_x = 0
    # fill the screen and draw all elements
    screen.blit(bg_surface, (0, 0))
    screen.blit(forest_surface, (forest_surface_x, 0))
    screen.blit(forest_surface, (forest_surface_x + screen_width, 0))
    screen.blit(floor_surface, (floor_surface_x, 0))
    screen.blit(floor_surface, (floor_surface_x + screen_width, 0))

    pygame.display.update()
    clock.tick(120)
