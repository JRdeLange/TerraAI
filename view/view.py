#from world.world import World
from pygame_toolkit.pygame_toolkit import PygameToolkit
from vecmath.Vec2D import Vec2D
import config
import pygame


class View:

    def __init__(self, world):
        self.tk = PygameToolkit()
        self.size = Vec2D(config.window_width, config.window_height)
        self.window, self.clock = self.tk.init_pygame(self.size.x, self.size.y, "TerraAI")

        self.world = world

        self.cache_sprites()

    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        self.tk.clear(color=[30, 150, 30])
        self.draw()
        pygame.display.flip()
        self.clock.tick(60)

    def draw(self):
        self.draw_agents()

    def draw_agents(self):
        for agent in self.world.get_agents:
            sprite_name = "team_" + str(agent.team)
            self.tk.render_sprite(sprite_name, self.transform_pos(agent.pos))

    def cache_sprites(self):
        self.tk.add_sprite("team_0", path="./assets/green.png", size=Vec2D(2, 2))
        self.tk.add_sprite("team_1", path="./assets/red.png", size=Vec2D(2, 2))

    def transform_pos(self, world_space):
        world_space /= Vec2D(self.world.get_width, self.world.get_height)
        screen_space = world_space * self.size
        return screen_space
