from Game.Organisms.Animal import Animal
from Game.Organisms.Organism import Organism
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World
from Utils.interruptedActionException import InterruptedActionException


class Turtle(Animal):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.turtle
        self.strength = 2
        self.initiative = 1

    def collision(self, collider: Organism, isAttacker=False):
        if collider.strength < 5:
            raise InterruptedActionException("")

        super().collision(collider, isAttacker)
