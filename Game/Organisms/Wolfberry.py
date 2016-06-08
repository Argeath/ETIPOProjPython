from Game.Organisms.Organism import Organism
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.Organisms.Plant import Plant
from Game.World import World


class Wolfberry(Plant):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.wolfberry

    def collision(self, collider: Organism, isAttacker=False):
        collider.dieing = True
        self.dieing = True
