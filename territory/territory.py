class Territory:

    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

        # variables that will be set when populating the world
        self.owner = None
        self. neighbours = []

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
