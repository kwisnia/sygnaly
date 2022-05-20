from distance.DistanceSensor import DistanceSensor
from distance.Environment import Environment
from gui.MainWindow import MainWindow
import sys
from PySide6 import QtWidgets
from functions import *
from filters import *


if __name__ == "__main__":
    # app = QtWidgets.QApplication([])

    # widget = MainWindow()
    # widget.show()

    # sys.exit(app.exec())

    sensor = DistanceSensor(1, 20, 60, 0.5)
    env = Environment(0.1, 100, 0.5, sensor, 25)

    for i in range(0, 10000):
        env.step()
        print(sensor.distance)