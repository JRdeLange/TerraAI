import config
from territory.territory import Territory


class World:

    def __init__(self):
        self.world_size = config.world_size
        self.territory_grid = []

        # create a grid of territories
        for x in range(self.world_size):
            column = []
            for y in range(self.world_size):
                column.append(Territory(x, y))
            self.territory_grid.append(column)

        # for each territory in the grid, set its neighbours
        for x in range(self.world_size):
            for y in range(self.world_size):
                self.territory_grid[x][y].set_neighbours(self.get_neighbouring_territories(self.territory_grid[x][y]))

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
