import random

from Game.Organisms.Organism import Organism
from Game.World import World


class Plant(Organism):
    def __init__(self, w: World):
        super().__init__(w)

    def action(self):
        r = random.randint(0, 100)
        #if r < 4:
        #    self.breed()
