import math


class Hexagon:

    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color
        self.vertices = self.calc_vertices()

    def calc_vertices(self):
        vertices = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = angle_deg * (3.14159 / 180)
            x = self.position[0] + self.size * math.cos(angle_rad)
            y = self.position[0] + self.size * math.sin(angle_rad)
            vertices.append((x, y))
        return vertices
