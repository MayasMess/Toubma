import pygame


class Player:
    def __init__(self, screen, screen_width, screen_heigth):
        self.screen = screen
        self.player = [
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
        self.player_pos_x = 0
        self.player_pos_y = screen_heigth / 2 + 90

    def player_run(self, frame_count):
        self.screen.blit(self.player[frame_count // (120 // len(self.player))], (0, self.player_pos_y))

