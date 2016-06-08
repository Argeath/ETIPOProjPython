from Game.Organisms.Organism import Organism
from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World
from Utils.Direction import Direction
from Utils.interruptedActionException import InterruptedActionException


class Animal(Organism):
    def __init__(self, w: World):
        super().__init__(w)

    def action(self):
        if self.dieing:
            return

        d = self.getRandomDirection()

        if (d == Direction.NONE).all():
            return

        self.move(d)

    def move(self, d):
        if self.dieing:
            return

        try:
            newPos = self.position + d
            if 0 <= newPos[0] < self.world.size[0] and 0 <= newPos[1] < self.world.size[1]:
                collider = self.world.getOrganismOnPos(newPos)
                if collider is not None:
                    self.collision(collider, True)

                self.world.moveOrganism(self, d)
        except InterruptedActionException:
            pass

    def collision(self, collider: Organism, isAttacker=False):
        if self.type == collider.type and self.type != OrganismTypes.human and self.age > 10 and collider.age > 10:
            self.breed()
            raise InterruptedActionException("")

        if self.type == collider.type:
            raise InterruptedActionException("")

        if isAttacker:
            collider.collision(self)

        if self.strength > collider.strength or isAttacker and self.strength >= collider.strength:
            collider.dieing = True
            collider.onDie()

            self.world.addToLogs(self.type.name + " killed " + collider.type.name + ".")

        elif self.strength < collider.strength and isAttacker:
            self.dieing = True
            self.onDie()

            self.world.addToLogs(self.type.name + " attacked " + collider.type.name + " and died.")
