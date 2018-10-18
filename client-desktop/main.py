#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget # pylint: disable=E0611

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Haweb')
    w.show()
    sys.exit(app.exec_())