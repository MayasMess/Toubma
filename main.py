import time

import pygame
import sys
from background.background import Background
pygame.init()
screen_width = 768
screen_height = 448
screen = pygame.display.set_mode((screen_width, screen_height))
from player.player import Player
from  player.player import PlayerMovements
from  player.player import PlayerActions

clock = pygame.time.Clock()
white = (255, 255, 255)
frame_count = 1
background = Background(screen=screen, screen_width=screen_width, screen_height=screen_height)
player = Player(screen=screen, screen_width=screen_width, screen_heigth=screen_height)
keys = []
action = PlayerMovements.RUN
mouvement = PlayerActions.NONE
pygame.key.set_repeat(0)
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

    mouvement = PlayerMovements.NONE
    action = PlayerActions.NONE

    if key_down:
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            action = PlayerActions.JUMP

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        mouvement = PlayerMovements.MOVE_FORWARD

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        mouvement = PlayerMovements.MOVE_BACKWARD

    background.move()
    player.animate(action=action, mouvement=mouvement, frame_count=frame_count)
    pygame.display.update()
    frame_count += 1
    clock.tick(120)

