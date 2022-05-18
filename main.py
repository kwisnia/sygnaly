from copy import deepcopy
from SignalFactory import SignalFactory
from gui.test_window import MainWindow
import sys
from PySide6 import QtWidgets
from functions import *
from filters import *
from operations import convolve
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, sosfilt, chirp, firwin


if __name__ == "__main__":
    # app = QtWidgets.QApplication([])

    # widget = MainWindow()
    # # widget.resize(800, 700)
    # widget.show()

    # sys.exit(app.exec())
    first_signal = SignalFactory().create(
        amplitude=2.0,
        frequency=1,
        sample_rate=1000,
        signal_duration=10,
        signal_start_time=0,
        type_of_signal=generate_sinusoidal_signal,
    )
    aaa = firwin(31, 450, window='boxcar', fs=1000)
    filtered = lfilter(aaa, 1, first_signal.values)
    filter = low_pass_filter(31, 450, window_type=0, sample_rate=1000)
    second_signal = deepcopy(first_signal)
    second_signal.values = filter
    second_signal.samples = second_signal.samples[:len(second_signal.values)]
    test = convolve(second_signal, first_signal)
    plt.plot(first_signal.samples, filtered, label="filtered scipy")
    plt.plot(first_signal.samples, first_signal.values, label="original")
    plt.plot(test.samples, test.values, label="convolved")
    plt.legend()
    plt.show()
