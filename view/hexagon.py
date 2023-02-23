import math


class Hexagon:

    def __init__(self, size, territory):
        self.size = size
        self.territory = territory
        self.position = self.calc_position()
        self.vertices = self.calc_vertices()

    def calc_position(self):
        x = self.territory.x_coordinate
        y = self.territory.y_coordinate
        print(x, y)
        return [x * self.size * 2, y * self.size * 2]

    def calc_vertices(self):
        vertices = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = angle_deg * (3.14159 / 180)
            x = self.position[0] + self.size * math.cos(angle_rad)
            y = self.position[1] + self.size * math.sin(angle_rad)
            vertices.append((x, y))
        return vertices

    def get_color(self):
        #return self.territory.get_color
        return [255, 255, 255]

    def get_vertices(self):
        return self.vertices
