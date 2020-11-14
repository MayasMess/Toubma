import time

import pygame
import sys
from background.background import Background
from player.player import Player

pygame.init()
screen_width = 768
screen_height = 448
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
white = (255, 255, 255)

frame_count = 1
background = Background(screen=screen, screen_width=screen_width, screen_height=screen_height)
player = Player(screen=screen, screen_width=screen_width, screen_heigth=screen_height)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if frame_count > 119:
        frame_count = 1
    background.move()
    player.run(frame_count)
    pygame.display.update()
    frame_count += 1
    clock.tick(120)

