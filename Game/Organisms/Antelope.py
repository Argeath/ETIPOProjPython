import random

from Game.Organisms.Animal import Animal
from Game.Organisms.Organism import Organism
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World


class Antelope(Animal):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.antelope
        self.strength = 4
        self.initiative = 4

    def action(self):
        super().action()
        super().action()

    def collision(self, collider: Organism, isAttacker=False):
        if not isAttacker and collider.type != self.type:
            r = random.randint(0, 100)
            if r < 50:
                super().action()
                return

        super().collision(collider, isAttacker)
