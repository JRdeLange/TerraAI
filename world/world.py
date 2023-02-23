import config
from territory.territory import Territory


class World:

    def __init__(self):
        self.world_size = config.world_size
        self.territory_grid = []

        for x in range(self.world_size):
            column = []
            for y in range(self.world_size):
                column.append(Territory(x, y))
            self.territory_grid.append(column)

    def get_territory(self, x, y):
        return self.territory_grid[x][y]

    def get_neighbouring_territories(self, territory):
        neighbours = []
        x = territory.x_coordinate
        y = territory.y_coordinate

        # Get the neighbour above the territory
        neighbours.append(self.territory_grid[x][y + 1])
        # Get the neighbours up and left and up and right of the territory
        neighbours.append(self.territory_grid[x + 1][y])
        neighbours.append(self.territory_grid[x - 1][y])
        # Get the three neighbours below the territory
        neighbours.append(self.territory_grid[x + 1][y - 1])
        neighbours.append(self.territory_grid[x][y - 1])
        neighbours.append(self.territory_grid[x - 1][y - 1])

        return neighbours
