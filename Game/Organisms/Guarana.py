from Game.Organisms.Organism import Organism
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.Organisms.Plant import Plant
from Game.World import World


class Guarana(Plant):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.guarana

    def collision(self, collider: Organism, isAttacker=False):
        collider.strength += 3
