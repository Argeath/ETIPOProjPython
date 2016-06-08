import random

import numpy as np
from PyQt5.QtWidgets import QTextEdit

from Game.Organisms.Organism import Organism
from Game.Organisms.OrganismTypes import OrganismTypes
from Utils.Direction import Direction


class World:
    def __init__(self, s, panel, logOutput : QTextEdit):
        self.size = s
        self.gamePanel = panel
        self.logOutput = logOutput
        self.organismMap = [[None for x in range(s[0])] for y in range(s[1])]
        self.human = None
        self.finished = False
        self.organisms = [[] for y in range(7)]
        self.toBorn = []

        for x in range(7):
            self.organisms.append([])

    def __getstate__(self):
        d = dict(self.__dict__)
        del d['gamePanel']
        del d['logOutput']
        return d

    def __setstate__(self, d):
        self.__dict__.update(d)

    def addToLogs(self, s: str):
        self.logOutput.append(s)

    def init(self):
        self.human = self.createOrganism(OrganismTypes.human)
        self.createRandomOrganisms()

    def createRandomOrganisms(self):
        rozmiar = np.ceil(np.sqrt(self.size[0] * self.size[1]) / 3)

        for name, member in OrganismTypes.__members__.items():
            if member == OrganismTypes.human:
                continue

            amount = random.randint(0, rozmiar)
            for x in range(amount):
                self.createOrganism(member)
                pass

    def addOrganism(self, organism: Organism):
        if self.getOrganismOnPos(organism.position) is None:
            self.toBorn.append(organism)
            self.organismMap[organism.position[1]][organism.position[0]] = organism

    def getOrganismOnPos(self, pos) -> Organism:
        return self.organismMap[pos[1]][pos[0]]

    def moveOrganism(self, organism: Organism, d: Direction):
        self.organismMap[organism.position[1]][organism.position[0]] = None

        newPos = organism.position + d

        organism.position = newPos
        self.organismMap[newPos[1]][newPos[0]] = organism

    def createOrganism(self, t: OrganismTypes, x: int = -1, y: int = -1) -> Organism:
        organism = Organism.getOrganismByType(self, t)
        if organism is None:
            return None

        if x == -1 or y == -1:
            posX, posY, attempts = 0, 0, 0

            while True:
                posX = random.randint(0, self.size[0] - 1)
                posY = random.randint(0, self.size[1] - 1)

                if self.getOrganismOnPos([posX, posY]) is None or ++attempts >= 5:
                    break

            if attempts >= 5:
                return None

            x = posX
            y = posY

        organism.position = [x, y]
        self.addOrganism(organism)
        return organism

    def render(self):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if self.organismMap[y][x] is None:
                    (self.gamePanel.fields[y][x]).type = OrganismTypes.none
                else:
                    (self.gamePanel.fields[y][x]).type = (self.organismMap[y][x]).type
                (self.gamePanel.fields[y][x]).repaint()

    def round(self, keyChar: str):
        if self.finished:
            return

        for v in self.organisms:
            for o in v:
                if o.dieing:
                    continue

                o.age += 1
                o.action()

                if o.type == OrganismTypes.human:
                    o.handleInput(keyChar)

        for v in self.organisms:
            for o in list(v):
                if o.dieing:
                    if self.organismMap[o.position[1]][o.position[0]] == o:
                        self.organismMap[o.position[1]][o.position[0]] = None
                    v.remove(o)

        for o in self.toBorn:
            self.organisms[o.initiative].append(o)

        self.toBorn.clear()

        self.render()
