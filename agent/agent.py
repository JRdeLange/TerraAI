from vecmath import Vec2D
from vecmath import vecmath


class Agent:

    def __init__(self, pos):
        self.pos = pos
        self.direction = vecmath.random_direction_vector()

    def tick(self):
        self.move()

    def move(self):
        self.pos += self.direction
