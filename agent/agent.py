import config
from vecmath import Vec2D
from vecmath import vecmath


class Agent:

    def __init__(self, id, pos, team):
        self.id = id
        self.pos = pos
        self.team = team
        self.direction = vecmath.random_direction_vector()

        self.speed = config.standard_agent_speed
        self.radius = config.standard_agent_radius
        self.health = config.standard_agent_health
        self.view_range = config.standard_agent_view_range

    def tick(self, observations):
        for observation in observations:
            if observation.get_team() != self.team:
                pass
        self.move()

    def move(self):
        self.pos += self.direction + self.speed

    def get_team(self):
        return self.team

    def get_pos(self):
        return self.pos

    def get_view_range(self):
        return self.view_range
