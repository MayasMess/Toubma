import pygame
from enum import Enum


class PlayerActions(Enum):
    NONE = 0
    JUMP = 1,
    DOUBLE_JUMP = 2,


class PlayerMovements(Enum):
    NONE = 3
    RUN = 1,
    MOVE_FORWARD = 2,
    MOVE_BACKWARD = 3,



class Player:
    player_run_animation = [
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-run-00.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-run-01.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-run-02.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-run-03.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-run-04.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-run-05.png').convert_alpha()),
    ]

    player_jump_animation = [
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-jump-00.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-jump-01.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-jump-02.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-jump-03.png').convert_alpha())
    ]

    player_double_jump_animation = [
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-smrslt-00.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-smrslt-01.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-smrslt-02.png').convert_alpha()),
        pygame.transform.scale2x(pygame.image.load(
            'player/assets/Adventurer-1.5/Individual Sprites/adventurer-smrslt-03.png').convert_alpha()),
    ]

    jump_height = 1

    def __init__(self, screen, screen_width, screen_heigth):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_heigth

        self.player_base_pos_x = 0
        self.player_pos_x = self.player_base_pos_x

        self.player_base_pos_y = screen_heigth / 2 + 90
        self.player_pos_y = self.player_base_pos_y

        self.moving_forward = False
        self.moving_backward = False

        self.jump_frame_count = 0
        self.jumping = False

        self.double_jump_frame_count = 0
        self.double_jumping = False
        self.descending = False

    def init(self):
        self.moving_forward = False
        self.moving_backward = False
        self.jumping = False
        self.double_jumping = False

    def animate(self, action, mouvement, frame_count):
        if action == PlayerMovements.RUN:
            self.run(frame_count=frame_count, mouvement=mouvement)
        if action == PlayerActions.JUMP:
            if not self.jumping:
                self.jumping = True
            else:
                self.descending = False
                self.double_jumping = True

        if mouvement == PlayerMovements.MOVE_FORWARD:
            self.move_forward()
        if mouvement == PlayerMovements.MOVE_BACKWARD:
            self.move_backward()

        if self.double_jumping:
            self.double_jump()
        elif self.jumping:
            self.jump()
        else:
            self.run(frame_count=frame_count, mouvement=mouvement)

    def move_forward(self):
        if self.player_pos_x < self.screen_width:
            self.player_pos_x += 1

    def move_backward(self):
        if self.player_pos_x > 0:
            self.player_pos_x -= 1

    def run(self, frame_count, mouvement):
        if mouvement == PlayerMovements.MOVE_FORWARD:
            if frame_count > 59:
                frame_count -= 60
            animation_index = (frame_count // (60 // len(self.player_run_animation)))
        elif mouvement == PlayerMovements.MOVE_BACKWARD:
            if frame_count < 59:
                frame_count += 60
            animation_index = (frame_count // (240 // len(self.player_run_animation)))
        else:
            animation_index = frame_count // (120 // len(self.player_run_animation))
        self.screen.blit(self.player_run_animation[animation_index],
                         (self.player_pos_x, self.player_pos_y))

    def jump(self):
        self.jump_frame_count += 1
        if self.jump_frame_count > 119:
            self.jump_frame_count = 1
        if self.jump_frame_count > 59:
            self.descending = True
        if self.player_pos_y == self.player_base_pos_y:
            self.double_jumping = False
            self.jump_frame_count = 0
            self.jumping = False
            self.jump_frame_count = 0
            self.descending = False
        # animation_index = self.jump_frame_count // (120 // len(self.player_jump_animation))
        if self.descending:
            self.player_pos_y += self.jump_height
        elif self.jump_frame_count < 60:
            self.player_pos_y -= self.jump_height
        else:
            self.player_pos_y += self.jump_height

        self.screen.blit(self.player_jump_animation[self.jump_frame_count // (120 // len(self.player_jump_animation))],
                         (self.player_pos_x, self.player_pos_y))

    def double_jump(self):
        self.double_jump_frame_count += 1
        if self.double_jump_frame_count > 119:
            self.double_jump_frame_count = 1
        if self.double_jump_frame_count > 59:
            self.descending = True
        if self.player_pos_y == self.player_base_pos_y:
            self.double_jumping = False
            self.double_jump_frame_count = 0
            self.jumping = False
            self.jump_frame_count = 0
            self.descending = False
        # animation_index = self.double_jump_frame_count // (120 // len(self.player_double_jump_animation))
        if self.descending:
            self.player_pos_y += self.jump_height
        elif self.double_jump_frame_count < 60:
            self.player_pos_y -= self.jump_height
        else:
            self.player_pos_y += self.jump_height

        self.screen.blit(self.player_double_jump_animation[
                             self.double_jump_frame_count // (120 // len(self.player_double_jump_animation))],
                         (self.player_pos_x, self.player_pos_y))
