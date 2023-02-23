import config
from territory.territory import Territory
from lord.lord import Lord


class World:

    def __init__(self):
        self.world_size = config.world_size
        self.number_of_lords = config.number_of_lords
        self.territory_grid = []
        self.lords = []
        self.lord_colors = config.lord_colors
        self.lord_names = config.lord_names

        # initialize territory grid
        for x in range(self.world_size):
            column = []
            for y in range(self.world_size):
                column.append(Territory(x, y))
            self.territory_grid.append(column)

        # initialize neighbours
        for x in range(self.world_size):
            for y in range(self.world_size):
                self.territory_grid[x][y].set_neighbours(self.get_neighbouring_territories(self.territory_grid[x][y]))

        # initialize lords
        for x in range(self.number_of_lords):
            self.lords.append(Lord(x, self.lord_names[x], self.lord_colors[x]))

    def get_territory(self, x, y):
        return self.territory_grid[x][y]

    def get_neighbouring_territories(self, territory):
        neighbours = []
        x = territory.x_coordinate
        y = territory.y_coordinate

        # Get the neighbour above the territory
        if not y == (self.world_size - 1):
            neighbours.append(self.territory_grid[x][y + 1])
        else:
            neighbours.append(None)
        # Get the neighbours up and left and up and right of the territory
        if not x == 0:
            neighbours.append(self.territory_grid[x - 1][y])
        else:
            neighbours.append(None)
        if not x == (self.world_size - 1):
            neighbours.append(self.territory_grid[x + 1][y])
        else:
            neighbours.append(None)
        # Get the three neighbours below the territory
        if not y == 0:
            neighbours.append(self.territory_grid[x][y - 1])
        else:
            neighbours.append(None)
        if not x == 0 and not y == 0:
            neighbours.append(self.territory_grid[x - 1][y - 1])
        else:
            neighbours.append(None)
        if not x == (self.world_size - 1) and not y == 0:
            neighbours.append(self.territory_grid[x + 1][y - 1])
        else:
            neighbours.append(None)

        return neighbours
