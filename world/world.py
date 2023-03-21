import config
import vecmath.vecmath as vm


class World:

    def __init__(self):
        self.agents = []
        self.height = config.world_height
        self.width = config.world_width

    def init_agents:
        for x in range(config.number_of_agents):
            pos = vm.random_vector_2d(self.width, self.height)
    def tick(self):
        for agent in self.agents:
            agent_pos = agent.get_pos()
            agent_view_range = agent.get_view_range()

    def get_agents(self):
        return self.agents