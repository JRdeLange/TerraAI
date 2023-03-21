import config
import random
import vecmath.vecmath as vm
from agent.agent import Agent
import math


class World:

    def __init__(self):
        self.agents = []
        self.height = config.world_height
        self.width = config.world_width

        self.init_agents()

    def init_agents(self):
        for x in range(config.number_of_agents):
            pos = vm.random_vector_2d(self.width, self.height)
            team = random.randint(0, 1)
            new_agent = Agent(pos, team)
            self.agents.append(new_agent)

    def tick(self):
        for agent in self.agents:
            agent.move()
            agent_pos = agent.get_pos()
            agent_view_range = agent.get_view_range()

    def get_agents(self):
        return self.agents

    def get_world_height(self):
        return self.height

    def get_world_width(self):
        return self.width