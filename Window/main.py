import sys

from PyQt5.QtGui import (QImage, QImageReader)
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QApplication, QTextEdit)

from Game.Organisms.OrganismTypes import OrganismTypes
from Window.gamePanel import GamePanel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    vBox = QVBoxLayout()

    mapSize = (20, 20)

    fieldSize = (33, 33)
    logsHeight = 5 * 20


    images = []

    for name, member in OrganismTypes.__members__.items():
        images.insert(member.value, QImage(QImageReader("images/" + name).read()))

    logOutput = QTextEdit()
    logOutput.setReadOnly(True)
    logOutput.setLineWrapMode(QTextEdit.NoWrap)
    logOutput.setFixedSize(mapSize[0] * fieldSize[0] + 33, logsHeight)

    font = logOutput.font()
    font.setFamily("Courier")
    font.setPointSize(10)

    gPanel = GamePanel(mapSize, images, logOutput)
    w = QWidget()
    w.setBaseSize(mapSize[0] * fieldSize[0], mapSize[1] * fieldSize[1] + logsHeight + 5)
    w.setWindowTitle('SymulETIr Świata - Dominik Kinal 160589')

    vBox.addWidget(gPanel)
    vBox.addWidget(logOutput)

    w.setLayout(vBox)
    w.move(600, 50)
    w.show()

    sys.exit(app.exec_())
