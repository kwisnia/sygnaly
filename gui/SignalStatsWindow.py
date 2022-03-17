from PySide6 import QtWidgets, QtCore

from Signal import Signal
from stats import (
    abs_avg_signal_value,
    avg_signal_power,
    avg_signal_value,
    rms_signal_value,
    variance_signal_value,
)


class SignalStatsWindow(QtWidgets.QWidget):
    def __init__(self, signal: Signal):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(
            QtWidgets.QLabel(f"Wartość średnia sygnału: {avg_signal_value(signal)}")
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Wartość średnia bezwzględna sygnału: {abs_avg_signal_value(signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(f"Moc średnia sygnału: {avg_signal_power(signal)}")
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Wariancja sygnału w przedziale wokół wartości średniej: {variance_signal_value(signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(f"Wartość skuteczna sygnału: {rms_signal_value(signal)}")
        )
