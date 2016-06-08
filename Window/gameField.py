from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QMenu)

from Game.Organisms.OrganismTypes import OrganismTypes


class GameField(QWidget):
    def __init__(self, position, images):
        super().__init__()

        self.position = position
        self.images = images
        self.initUI()
        self.type = OrganismTypes.none

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        actions = {}

        for name, member in OrganismTypes.__members__.items():
            actions[member.name] = menu.addAction(name)

        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action in list(actions.values()):
            index = list(actions.keys())[list(actions.values()).index(action)]
            animal = OrganismTypes[index]
            print(animal)

    def initUI(self):
        self.setFixedSize(33, 33)
        self.setContentsMargins(0, 0, 0, 0)

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):
        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRect(0, 0, 32, 32)
        if self.type != OrganismTypes.none:
            qp.drawImage(0, 0, self.images[self.type.value])
