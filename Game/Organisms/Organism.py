import random
from abc import abstractmethod

import numpy as np
from Utils.Direction import Direction
from Game.Organisms.OrganismTypes import OrganismTypes


class Organism:
    def __init__(self, world):
        self.type = OrganismTypes.none
        self.age = 0
        self.strength = 0
        self.initiative = 0
        self.dieing = False

        self.world = world
        self.position = np.array([0, 0])

    @abstractmethod
    def action(self):
        pass

    def collision(self, collider, isAttacker=False):
        pass

    def onDie(self):
        pass

    def getRandomDirection(self, mustBeEmpty=False) -> Direction:
        dirs = []

        for member in Direction.all:
            newPos = self.position + member

            if 0 <= newPos[0] < self.world.size[0] and 0 <= newPos[1] < self.world.size[1] and \
                    (not mustBeEmpty or self.world.getOrganismOnPos(newPos) is None):
                dirs.append(member)

        if len(dirs) == 0:
            return Direction.NONE

        r = random.randint(0, len(dirs) - 1)
        return dirs[r]

    def breed(self):
        d = self.getRandomDirection(True)
        if (d == Direction.NONE).all():
            return

        organism = Organism.getOrganismByType(self.world, self.type)
        if organism is None:
            return

        newPos = self.position + d

        self.world.createOrganism(self.type, newPos[0], newPos[1])

    @staticmethod
    def getOrganismByType(w, t: OrganismTypes):
        organism = None

        from Game.Organisms.Antelope import Antelope
        from Game.Organisms.Fox import Fox
        from Game.Organisms.Grass import Grass
        from Game.Organisms.Guarana import Guarana
        from Game.Organisms.Human import Human
        from Game.Organisms.Sheep import Sheep
        from Game.Organisms.SowThistle import SowThistle
        from Game.Organisms.Turtle import Turtle
        from Game.Organisms.Wolf import Wolf
        from Game.Organisms.Wolfberry import Wolfberry

        if t == OrganismTypes.antelope:
            organism = Antelope(w)
        elif t == OrganismTypes.fox:
            organism = Fox(w)
        elif t == OrganismTypes.grass:
            organism = Grass(w)
        elif t == OrganismTypes.guarana:
            organism = Guarana(w)
        elif t == OrganismTypes.human:
            organism = Human(w)
        elif t == OrganismTypes.sheep:
            organism = Sheep(w)
        elif t == OrganismTypes.sow_thistle:
            organism = SowThistle(w)
        elif t == OrganismTypes.turtle:
            organism = Turtle(w)
        elif t == OrganismTypes.wolf:
            organism = Wolf(w)
        elif t == OrganismTypes.wolfberry:
            organism = Wolfberry(w)

        return organism
