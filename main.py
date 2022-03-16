from gui.MainWindow import MainWindow
from plot import plot_continuous, plot_discrete
import PySide6.QtCore
import sys
from PySide6 import QtWidgets


if __name__ == "__main__":
    # signal_factory = SignalFactory()
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

    # signal = signal_factory.create(
    #     amplitude=1,
    #     signal_start_time=0,
    #     signal_duration=10,
    #     frequency=2,
    #     type_of_signal=fn.generate_unit_impulse,
    #     fullfilment=5,
    #     sample_rate=3,
    # )
    # plot_discrete(signal)
