import agent
import random
from vecmath import vecmath


class Soldier(agent):
    def __init__(self, agent_id, pos, team, death_function):
        super().__init__(agent_id, pos, team, death_function)

    def tick(self, observations):
        self.direction = vecmath.random_direction_vector()
        for observed_agent in observations:
            if observed_agent.get_team() != self.team:
                enemy_position = observed_agent.get_pos()
                if (enemy_position - self.pos).length() < 1:
                    self.fight(observed_agent)
                else:
                    self.charge(observed_agent.get_pos())

    def charge(self, position):
        self.direction = (position - self.pos).normalizad()

    def fight(self, enemy_agent):
        victory = random.randint(0, 1)
        if victory:
            enemy_agent.death_function(enemy_agent)
