from Game.Organisms.Animal import Animal
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World


class Sheep(Animal):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.sheep
        self.strength = 4
        self.initiative = 4
