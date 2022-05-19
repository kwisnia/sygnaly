from gui.MainWindow import MainWindow
import sys
from PySide6 import QtWidgets
from functions import *
from filters import *


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())