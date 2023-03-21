import config
import random
import vecmath.vecmath as vm
from agent.soldier import Soldier
import math


class World:

    def __init__(self):
        self.agents = []
        self.height = config.world_height
        self.width = config.world_width

        self.init_agents()

    def init_agents(self):
        agent_id = 0
        for x in range(config.number_of_agents):
            pos = vm.random_vector_2d(self.width, self.height)
            team = random.randint(0, 1)
            new_agent = Soldier(agent_id, pos, team, self.agent_died)
            self.agents.append(new_agent)
            agent_id = agent_id + 1

    def tick(self):
        for agent in self.agents:
            agent_pos = agent.get_pos()
            agent_view_range = agent.get_view_range()
            observations = self.observe_environment(agent_pos, agent_view_range)
            agent.tick(observations)

    def observe_environment(self, position, view_range):
        observations = []
        for agent in self.agents:
            if (agent.pos - position).length() < view_range:
                observations.append(agent)
        return observations

    def agent_died(self, agent):
        self.agents.remove(agent)

    def get_agents(self):
        return self.agents

    def get_world_height(self):
        return self.height

    def get_world_width(self):
        return self.width
