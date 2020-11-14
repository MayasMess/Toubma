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

    def __init__(self, screen, screen_width, screen_heigth):
        self.screen = screen
        self.player_pos_x = 0
        self.player_pos_y = screen_heigth / 2 + 90

    def run(self, frame_count):
        self.screen.blit(self.player_run_animation[frame_count // (120 // len(self.player_run_animation))], (0, self.player_pos_y))

    def jump(self, frame_count):
        self.screen.blit(self.player_run_animation[frame_count // (120 // len(self.player_run_animation))], (0, self.player_pos_y))

