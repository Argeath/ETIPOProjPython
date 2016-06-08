from Game.Organisms.OrganismTypes import OrganismTypes
from Game.World import World
from Window.gameField import GameField
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pickle


class GamePanel(QWidget):
    def __init__(self, size, images, logOutput):
        super().__init__()

        self.size = size
        self.images = images
        self.logOutput = logOutput

        self.shortcut = QShortcut(QKeySequence("A"), self)
        self.shortcut.activated.connect(self.moveWest)

        self.shortcut2 = QShortcut(QKeySequence("S"), self)
        self.shortcut2.activated.connect(self.moveSouth)

        self.shortcut3 = QShortcut(QKeySequence("W"), self)
        self.shortcut3.activated.connect(self.moveNorth)

        self.shortcut4 = QShortcut(QKeySequence("D"), self)
        self.shortcut4.activated.connect(self.moveEast)

        self.shortcut4 = QShortcut(QKeySequence("E"), self)
        self.shortcut4.activated.connect(self.castSpell)

        self.shortcut5 = QShortcut(QKeySequence("CTRL+S"), self)
        self.shortcut5.activated.connect(self.saveGame)

        self.shortcut6 = QShortcut(QKeySequence("CTRL+D"), self)
        self.shortcut6.activated.connect(self.loadGame)

        self.fields = [[0 for x in range(size[0])] for y in range(size[1])]
        self.initUI()

        self.world = World(size, self, logOutput)
        self.world.init()
        self.world.render()

    @pyqtSlot()
    def moveWest(self):
        self.world.round("A")

    @pyqtSlot()
    def moveSouth(self):
        self.world.round("S")

    @pyqtSlot()
    def moveNorth(self):
        self.world.round("W")

    @pyqtSlot()
    def moveEast(self):
        self.world.round("D")

    @pyqtSlot()
    def saveGame(self):
        with open("save.dat", "wb") as output:
            pickle.dump(self.world, output, pickle.HIGHEST_PROTOCOL)

    def loadGame(self):
        with open("save.dat", "rb") as input:
            self.world = pickle.load(input)
            self.world.gamePanel = self
            self.world.logOutput = self.logOutput
            self.world.render()

    @pyqtSlot()
    def castSpell(self):
        if self.world.human is not None:
            self.world.human.castSpell()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(1)
        self.setLayout(grid)

        positions = [(i, j) for i in range(self.size[1]) for j in range(self.size[0])]

        for position in positions:
            self.fields[position[0]][position[1]] = GameField(position, self.images)
            grid.addWidget(self.fields[position[0]][position[1]], *position)

        (self.fields[15][3]).type = OrganismTypes.fox
