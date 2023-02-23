class Territory:

    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

        # variables that will be set when populating the world
        self.owner = None
        self.neighbours = []

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours

    def get_neighbour(self, direction):
        if direction == "north":
            return self.neighbours[0]
        elif direction == "north-west":
            return self.neighbours[1]
        elif direction == "north-east":
            return self.neighbours[2]
        elif direction == "south":
            return self.neighbours[3]
        elif direction == "south-west":
            return self.neighbours[4]
        elif direction == "south-east":
            return self.neighbours[5]
        else:
            raise Exception("no such direction for territory neighbour")

    def get_color(self):
        if self.owner is None:
            return [255, 255, 255]
        else:
            return self.owner.get_color()
