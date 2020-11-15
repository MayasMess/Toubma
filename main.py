import pygame
import sys
from background.background import Background


pygame.init()
screen_width = 768
screen_height = 448
screen = pygame.display.set_mode((screen_width, screen_height))
from player.player import Player
from dialogs.dialogs import Dialogs
from  player.player import PlayerMovements
from  player.player import PlayerActions

clock = pygame.time.Clock()
white = (255, 255, 255)
frame_count = 1
background = Background(screen=screen, screen_width=screen_width, screen_height=screen_height)
player = Player(screen=screen, screen_width=screen_width, screen_heigth=screen_height)
dialog = Dialogs(screen=screen)

test_dialg = None
keys = []
action = PlayerMovements.RUN
mouvement = PlayerActions.NONE
pygame.key.set_repeat(0)
while True:
    keys = pygame.key.get_pressed()
    key_down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                dialog.go_to_next_step()
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

    if keys[pygame.K_h]:
        test_dialg = True
        dialog.start_dialog = True

    if test_dialg is True:
        dialog.test_dialog()

    print(dialog.dialog_count)

    player.animate(action=action, mouvement=mouvement, frame_count=frame_count)
    pygame.display.update()
    frame_count += 1
    clock.tick(120)

