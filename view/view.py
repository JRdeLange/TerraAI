from world.world import World
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
        pass

    def draw_hexagon(self, hexagon):
        pygame.draw.polygon(hexagon)

    def clear(self):
        self.window.fill((255, 255, 255))


