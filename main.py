from gui.MainWindow import MainWindow
import sys
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 700)
    widget.show()

    sys.exit(app.exec())
