from vecmath.Vec2D import Vec2D
import config


class Collisionator:

    def __init__(self, world):
        self.world = world

        self.coll_cell_size = config.collision_biggest_agent
        self.coll_map_size = Vec2D(int(self.world.get_world_width() / self.coll_cell_size),
                                   int(self.world.get_world_height() / self.coll_cell_size))
        self.coll_map_size += 1

        self.collision_map = [[CollisionCell() for x in range(self.coll_map_size.x)]
                              for y in range(self.coll_map_size.y)]

        self.make_collision_cells()

    def make_collision_cells(self):
        self.collision_map = [[CollisionCell() for y in range(self.coll_map_size.y)]
                              for x in range(self.coll_map_size.x)]

        agents = self.world.get_agents()
        for agent in agents:
            x = int(agent.pos.x / self.coll_cell_size)
            y = int(agent.pos.y / self.coll_cell_size)

            self.collision_map[x][y].add_agent(agent)


class CollisionCell:

    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)
