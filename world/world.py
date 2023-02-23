import config
from territory.territory import Territory


class World:

    def __init__(self):
        self.world_size = config.world_size
        self.world_grid = []

        for x in range(self.world_size):
            for y in range(self.world_size):
                self.world_grid[x][y] = Territory()

        self.territories = []

    def get_territory(self, x, y):
        return self.world_grid[x][y]

    def get_neighbouring_territories(self, x, y):
        neighbours = []

        # Get the neighbour above the territory
        neighbours.append(self.world_grid[x][y + 1])
        # Get the neighbours up and left and up and right of the territory
        neighbours.append(self.world_grid[x + 1][y])
        neighbours.append(self.world_grid[x - 1][y])
        # Get the three neighbours below the territory
        neighbours.append(self.world_grid[x + 1][y - 1])
        neighbours.append(self.world_grid[x][y - 1])
        neighbours.append(self.world_grid[x - 1][y - 1])

        return neighbours
