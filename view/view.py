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

    def tick(self):
        self.clear()

        self.draw()

    def draw(self):
        self.draw_territories()

    def draw_territories(self):
        hexagon = Hexagon(50, [0, 0], [255, 0, 0])

    def draw_hexagon(self, hexagon):
        pygame.draw.polygon(self.window, hexagon.color, hexagon.vertices)

    def clear(self):
        self.window.fill((255, 255, 255))


