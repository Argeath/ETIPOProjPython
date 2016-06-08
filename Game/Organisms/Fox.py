import random

from Game.Organisms.Animal import Animal
from Game.Organisms.Organism import Organism
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World
from Utils.Direction import Direction
from Utils.interruptedActionException import InterruptedActionException


class Fox(Animal):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.fox
        self.strength = 3
        self.initiative = 7

    def collision(self, collider: Organism, isAttacker=False):
        if isAttacker and collider.strength > self.strength:
            if (self.getRandomDirection(True) != Direction.NONE).all():
                self.action()
            raise InterruptedActionException("")

        super().collision(collider, isAttacker)
