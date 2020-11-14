import pygame


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

    jump_height = 2

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
        self.double_jump_descending = False

    def init(self):
        self.moving_forward = False
        self.moving_backward = False

    def animate(self, keys, frame_count):
        self.init()
        if keys:
            if keys[pygame.K_SPACE]:
                if not self.jumping:
                    self.jumping = True
                    self.double_jumping = False
                else:
                    self.double_jumping = True
                    self.jumping = False
                    self.jump_frame_count = 0
            if keys[pygame.K_RIGHT]:
                self.moving_forward = True
            if keys[pygame.K_LEFT]:
                self.moving_backward = True
        if self.double_jumping:
            self.double_jump()
        elif self.jumping:
            self.jump()
        elif self.moving_forward:
            self.move_forward(frame_count=frame_count)
        elif self.moving_backward:
            self.move_backward(frame_count=frame_count)
        else:
            self.run(frame_count=frame_count)

    def move_forward(self, frame_count):
        if frame_count > 59:
            frame_count -= 60
        animation_index = (frame_count // (60 // len(self.player_run_animation)))
        if self.player_pos_x < self.screen_width:
            self.player_pos_x += 1
        self.screen.blit(self.player_run_animation[animation_index],
                         (self.player_pos_x, self.player_base_pos_y))

    def move_backward(self, frame_count):
        if frame_count < 59:
            frame_count += 60
        animation_index = ((frame_count) // (240 // len(self.player_run_animation)))
        if self.player_pos_x > 0:
            self.player_pos_x -= 1
        self.screen.blit(self.player_run_animation[animation_index],
                         (self.player_pos_x, self.player_base_pos_y))

    def run(self, frame_count):
        self.screen.blit(self.player_run_animation[frame_count // (120 // len(self.player_run_animation))],
                         (self.player_pos_x, self.player_base_pos_y))

    def jump(self):
        self.jump_frame_count += 1
        if self.jump_frame_count > 119:
            self.jumping = False
            self.jump_frame_count = 1
        animation_index = self.jump_frame_count // (120 // len(self.player_jump_animation))
        if animation_index == 0 | animation_index == 1:
            self.player_pos_y -= self.jump_height
        elif animation_index == 2 | animation_index == 3:
            self.player_pos_y += self.jump_height

        self.screen.blit(self.player_jump_animation[self.jump_frame_count // (120 // len(self.player_jump_animation))],
                         (self.player_pos_x, self.player_pos_y))

    def double_jump(self):
        self.double_jump_frame_count += 1
        if self.double_jump_frame_count > 119:
            self.double_jump_frame_count = 1
        if self.double_jump_frame_count > 59:
            self.double_jump_descending = True
        if self.player_pos_y == self.player_base_pos_y:
            self.double_jumping = False
            self.double_jump_frame_count = 0
            self.jumping = False
            self.jump_frame_count = 0
            self.double_jump_descending = False
        animation_index = self.double_jump_frame_count // (120 // len(self.player_double_jump_animation))
        if self.double_jump_descending:
            self.player_pos_y += self.jump_height
        elif animation_index == 2 | animation_index == 3:
            self.player_pos_y += self.jump_height
        elif animation_index == 0 | animation_index == 1:
            self.player_pos_y -= self.jump_height

        self.screen.blit(self.player_double_jump_animation[
                             self.double_jump_frame_count // (120 // len(self.player_double_jump_animation))],
                         (self.player_pos_x, self.player_pos_y))
