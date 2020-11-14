import time

import pygame
import sys
from background.background import Background
pygame.init()
screen_width = 768
screen_height = 448
screen = pygame.display.set_mode((screen_width, screen_height))
from player.player import Player

clock = pygame.time.Clock()
white = (255, 255, 255)
frame_count = 1
background = Background(screen=screen, screen_width=screen_width, screen_height=screen_height)
player = Player(screen=screen, screen_width=screen_width, screen_heigth=screen_height)
keys = []
while True:
    key_down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down = True
    if frame_count > 119:
        frame_count = 1
    if key_down | pygame.key.get_pressed()[pygame.K_RIGHT] | pygame.key.get_pressed()[pygame.K_LEFT] :
        keys = pygame.key.get_pressed()
    else:
        keys = []
    background.move()
    player.animate(keys=keys, frame_count=frame_count)
    pygame.display.update()
    frame_count += 1
    clock.tick(120)

