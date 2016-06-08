import numpy as np

from Game.Organisms.Animal import Animal
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World
from Utils.Direction import Direction


class Human(Animal):
    def __init__(self, w: World):
        super().__init__(w)
        self.type = OrganismTypes.human
        self.strength = 5
        self.initiative = 4
        self.toNextSpell = 0

    def action(self):
        pass

    def handleInput(self, keyCode: int):
        if keyCode == "A":
            self.move(Direction.WEST)
        elif keyCode == "W":
            self.move(Direction.NORTH)
        elif keyCode == "S":
            self.move(Direction.SOUTH)
        elif keyCode == "D":
            self.move(Direction.EAST)

        self.doSpell()

    def doSpell(self):
        if self.toNextSpell > 5:
            for y in range(-1, 1):
                for x in range(-1, 1):
                    if y == 0 and x == 0:
                        continue

                    newPos = self.position + np.array([x, y])
                    if 0 <= newPos[0] < self.world.size[0] and 0 <= newPos[1] < self.world.size[1]:
                        organism = self.world.getOrganismOnPos(newPos)
                        if organism is not None:
                            organism.dieing = True
                            self.world.addToLogs("You burner " + organism.type.name + ".")


        if self.toNextSpell > 0:
            self.toNextSpell -= 1

    def castSpell(self):
        if self.toNextSpell > 0:
            self.world.addToLogs("To next spell " + self.toNextSpell + " rounds.")
            return

        self.toNextSpell = 10

    def onDie(self):
        self.world.finished = True
        self.world.addToLogs("You lost. Game over.")

