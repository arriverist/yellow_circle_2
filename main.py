import sys
from random import randint
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt


class FlagMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.resize(600, 600)
        self.do_paint = False
        self.holst = []
        self.pushButton = QPushButton(self)
        self.pushButton.move(70, 150)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        colo = QColor(randint(0, 255),
                      randint(0, 255),
                      randint(0, 255))
        qp.setPen(QPen(colo, 8, Qt.SolidLine))
        qp.setBrush(QBrush(colo, Qt.SolidPattern))
        z = randint(0, 500)
        qp.drawEllipse(randint(0, 100),
                       randint(0, 100),
                       z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec_())