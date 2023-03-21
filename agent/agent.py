import config
from vecmath import Vec2D
from vecmath import vecmath


class Agent:

    def __init__(self, agent_id, pos, team, death_function):
        self.id = agent_id
        self.pos = pos
        self.team = team
        self.direction = vecmath.random_direction_vector()

        self.speed = config.standard_agent_speed
        self.health = config.standard_agent_health
        self.view_range = config.standard_agent_view_range

    def tick(self, observations):
        self.direction = vecmath.random_direction_vector()
        self.move()

    def move(self):
        self.pos += self.direction + self.speed

    def get_team(self):
        return self.team

    def get_pos(self):
        return self.pos

    def get_view_range(self):
        return self.view_range
