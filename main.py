from environment.environment import Environment
from world.world import World
from view.view import View


def main():
    world = World()
    environment = Environment(world)
    view = View(world)
    while True:
        view.tick()


if __name__ == "__main__":
    main()
