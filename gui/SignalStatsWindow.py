from PySide6 import QtWidgets, QtCore

from Signal import Signal
from stats import (
    abs_avg_signal_value,
    avg_signal_power,
    avg_signal_value,
    maximum_difference,
    mean_square_error,
    peak_signal_to_noise_ratio,
    rms_signal_value,
    signal_to_noise_ratio,
    variance_signal_value,
)


class SignalStatsWindow(QtWidgets.QWidget):
    def __init__(
        self,
        original_signal: Signal,
        reconstructed_signal: Signal,
        sampled_signal: Signal,
        quantized_signal: Signal,
    ):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Wartość średnia sygnału: {avg_signal_value(original_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Wartość średnia bezwzględna sygnału: {abs_avg_signal_value(original_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Moc średnia sygnału: {avg_signal_power(original_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Wariancja sygnału w przedziale wokół wartości średniej: {variance_signal_value(original_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Wartość skuteczna sygnału: {rms_signal_value(original_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"MSE kwantyzacji: {mean_square_error(sampled_signal, quantized_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Signal to noise ratio kwantyzacji: {signal_to_noise_ratio(sampled_signal, quantized_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Peak signal to noise ratio kwantyzacji: {peak_signal_to_noise_ratio(sampled_signal, quantized_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Maksymalna różnica kwantyzacji: {maximum_difference(sampled_signal, quantized_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"MSE rekonstrukcji: {mean_square_error(original_signal, reconstructed_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Signal to noise ratio: {signal_to_noise_ratio(original_signal, reconstructed_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Peak signal to noise ratio: {peak_signal_to_noise_ratio(original_signal, reconstructed_signal)}"
            )
        )
        self.layout.addWidget(
            QtWidgets.QLabel(
                f"Maksymalna różnica: {maximum_difference(original_signal, reconstructed_signal)}"
            )
        )
