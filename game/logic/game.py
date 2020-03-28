import os
from random import randint

import pygame

from game.implements.objects import Hero
from game.models.stats import Stats


class Rocket:
    width = 20
    height = 50

    def __init__(self, surface: pygame.Surface, color):
        self._surface = surface
        self._color = color
        self._x = self._surface.get_width() // 2 - self.width // 2
        self._y = self._surface.get_height()
        print(self._surface.get_height())

    def fly(self):
        pygame.draw.rect(self._surface, self._color, (self._x, self._y, self.width, self.height))
        self._y -= 3
        if self._y < -self.height:
            self._y = 600


class Game:
    screen_dim = (800, 600)
    keyboard_control = True
    fps = 60

    def __init__(self, base_stats: Stats, sprite_size: int):
        pygame.init()
        self._surface = pygame.display.set_mode(self.screen_dim)
        pygame.display.set_caption('MyRPG')
        self._left = pygame.Surface((self.screen_dim[0] // 2, self.screen_dim[1]))
        self._right = pygame.Surface((self.screen_dim[0] // 2, self.screen_dim[1]))
        self._hero_position = [1, 1]
        # self._background = pygame.Surface((400, 200))
        # self._hero = pygame.Surface((100, 100))
        # self._engine = GameEngine()
        self._sprite_size = sprite_size
        self._clock = pygame.time.Clock()
        # self._hero = self.create_hero(base_stats, sprite_size, self._hero_position)

    # @staticmethod
    # def create_hero(stats, sprite_size, hero_position):
    #     hero_sprite = Service.create_sprite(
    #         os.path.join('texture', 'Hero.png'), sprite_size
    #     )
    #     return Hero(
    #         hero_sprite, stats, hero_position
    #     )

    def run(self):

        self._left.fill((255, 255, 255))
        self._surface.blit(self._left, (0, 0))
        self._surface.blit(self._right, (self.screen_dim[0] // 2, 0))
        rocket_left = Rocket(self._left, (0, 0, 0))
        rocket_right = Rocket(self._right, (255, 255, 255))
        active_left = False
        active_right = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.pos[0] < self.screen_dim[0] // 2:
                        active_left = True
                        active_right = False
                    elif event.pos[0] > self.screen_dim[0] // 2:
                        active_right = True
                        active_left = False
            if active_left:
                self._left.fill((255, 255, 255))
                rocket_left.fly()
                self._surface.blit(self._left, (0, 0))
            elif active_right:
                self._right.fill((0, 0, 0))
                rocket_right.fly()
                self._surface.blit(self._right, (self.screen_dim[0] // 2, 0))

            pygame.display.update()
