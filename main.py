from gui.MainWindow import MainWindow
import PySide6.QtCore
import sys
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

