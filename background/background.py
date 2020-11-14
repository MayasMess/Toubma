import pygame

class Background:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bg_surface = pygame.image.load(
            'background/assets/country-platform-files/country-platform-files/layers/country-platform-back.png').convert()
        self.bg_surface = pygame.transform.scale2x(self.bg_surface)

        self.forest_surface = pygame.image.load(
            'background/assets/country-platform-files/country-platform-files/layers/forest_transp.png').convert_alpha()
        self.forest_surface = pygame.transform.scale2x(self.forest_surface)
        self.forest_surface_x = 0

        self.floor_surface = pygame.image.load(
            'background/assets/country-platform-files/country-platform-files/layers/country-platform-tiles-example.png').convert_alpha()
        self.floor_surface = pygame.transform.scale2x(self.floor_surface)
        self.floor_surface_x = 0

    def move(self):
        self.forest_surface_x -= 0.17
        if self.forest_surface_x <= -self.screen_width:
            self.forest_surface_x = 0
        self.floor_surface_x -= 0.85
        if self.floor_surface_x <= -self.screen_width:
            self.floor_surface_x = 0

        self.screen.blit(self.bg_surface, (0, 0))
        self.screen.blit(self.forest_surface, (self.forest_surface_x, 0))
        self.screen.blit(self.forest_surface, (self.forest_surface_x + self.screen_width, 0))
        self.screen.blit(self.floor_surface, (self.floor_surface_x, 0))
        self.screen.blit(self.floor_surface, (self.floor_surface_x + self.screen_width, 0))
