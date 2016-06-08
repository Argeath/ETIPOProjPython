from Game.Organisms.OrganismTypes import OrganismTypes
from Game.Organisms.Plant import Plant
from Game.World import World


class Grass(Plant):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.grass
