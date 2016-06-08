from Game.Organisms.Animal import Animal
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World


class Wolf(Animal):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.wolf
        self.strength = 9
        self.initiative = 5
