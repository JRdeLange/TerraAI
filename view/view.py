from world.world import World
from view.hexagon import Hexagon
import config
import pygame


class View:

    def __init__(self, world):
        pygame.init()
        self.world = world
        self.width = config.window_width
        self.height = config.window_height
        self.window = pygame.display.set_mode([self.width, self.height])
        self.hex_size = self.width - config.window_padding * 2

        self.hexagons = []
        self.initialize_hexagons()

    def tick(self):
        self.clear()

        self.draw()
        pygame.display.flip()

    def draw(self):
        self.draw_territories()

    def draw_territories(self):
        for hexagon in self.hexagons:
            self.draw_hexagon(hexagon)

    def draw_hexagon(self, hexagon):
        pygame.draw.polygon(self.window, hexagon.get_color(), hexagon.get_vertices())

    def clear(self):
        self.window.fill([130, 130, 130])

    def initialize_hexagons(self):
        for x in range(config.world_size):
            for y in range(config.world_size):
                territory = self.world.get_territory(x, y)
                hexagon = Hexagon(15, territory)
                self.hexagons.append(hexagon)





