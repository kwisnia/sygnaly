from PySide6 import QtWidgets, QtCore
from plot import plot_continuous, plot_discrete
from SignalFactory import SignalFactory
from functions import *


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.signal_factory = SignalFactory()

        self.signals = [
            "Szum o rozkładzie jednostajnym",
            "Szum gaussowski",
            "Sygnał sinusoidalny",
            "Sygnał sinusoidalny wyprostowany jednopołówkowo",
            "Sygnał sinusoidalny wyprostowany dwupołówkowo",
            "Sygnał prostokątny",
            "Sygnał prostokątny symetryczny",
            "Sygnał trójkątny",
            "Skok jednostkowy",
            "Impuls jednostkowy",
            "Szum impulsowy",
        ]

        self.first_signal = QtWidgets.QComboBox()
        self.first_signal_type = generate_gauss_noise
        self.first_signal.addItems(self.signals)
        self.second_signal = QtWidgets.QComboBox()
        self.second_signal.addItems(self.signals)
        self.first_signal.currentIndexChanged.connect(self.show_first_signal_fields)
        self.second_signal.currentIndexChanged.connect(self.show_second_singal_fields)
        self.first_signal_start = QtWidgets.QDoubleSpinBox()
        self.second_signal_start = QtWidgets.QDoubleSpinBox()
        self.first_signal_length = QtWidgets.QDoubleSpinBox()
        self.second_signal_length = QtWidgets.QDoubleSpinBox()
        self.first_amplitude = QtWidgets.QDoubleSpinBox()
        self.second_amplitude = QtWidgets.QDoubleSpinBox()
        self.first_frequency = QtWidgets.QDoubleSpinBox()
        self.second_frequency = QtWidgets.QDoubleSpinBox()
        self.first_fullfilment = QtWidgets.QDoubleSpinBox()
        self.second_fullfilment = QtWidgets.QDoubleSpinBox()
        self.first_sample_rate = QtWidgets.QDoubleSpinBox()
        self.second_sample_rate = QtWidgets.QDoubleSpinBox()
        self.first_signal_start_text = QtWidgets.QLabel("Początek sygnału")
        self.second_signal_start_text = QtWidgets.QLabel("Początek sygnału")
        self.first_signal_length_text = QtWidgets.QLabel("Długość sygnału")
        self.second_signal_length_text = QtWidgets.QLabel("Długość sygnału")
        self.first_amplitude_text = QtWidgets.QLabel("Amplituda")
        self.second_amplitude_text = QtWidgets.QLabel("Amplituda")
        self.first_frequency_text = QtWidgets.QLabel("Częstotliwość")
        self.second_frequency_text = QtWidgets.QLabel("Częstotliwość")
        self.first_fullfilment_text = QtWidgets.QLabel("Długość okresu")
        self.second_fullfilment_text = QtWidgets.QLabel("Długość okresu")
        self.first_sample_rate_text = QtWidgets.QLabel("Częstotliwość próbkowania")
        self.second_sample_rate_text = QtWidgets.QLabel("Częstotliwość próbkowania")
        self.first_signal_generate = QtWidgets.QPushButton("Generuj sygnał")
        self.second_signal_generate = QtWidgets.QPushButton("Generuj sygnał")

        self.first_signal_generate.clicked.connect(self.generate_first_signal)

        first_signal_components = [
            QtWidgets.QLabel("Typ pierwszego sygnału"),
            self.first_signal,
            self.first_signal_start_text,
            self.first_signal_start,
            self.first_signal_length_text,
            self.first_signal_length,
            self.first_amplitude_text,
            self.first_amplitude,
            self.first_frequency_text,
            self.first_frequency,
            self.first_fullfilment_text,
            self.first_fullfilment,
            self.first_sample_rate_text,
            self.first_sample_rate,
            self.first_signal_generate,
        ]

        second_signal_components = [
            QtWidgets.QLabel("Typ drugiego sygnału"),
            self.second_signal,
            self.second_signal_start_text,
            self.second_signal_start,
            self.second_signal_length_text,
            self.second_signal_length,
            self.second_amplitude_text,
            self.second_amplitude,
            self.second_frequency_text,
            self.second_frequency,
            self.second_fullfilment_text,
            self.second_fullfilment,
            self.second_sample_rate_text,
            self.second_sample_rate,
            self.second_signal_generate,
        ]

        self.layout = QtWidgets.QGridLayout(self)

        for index, widget in enumerate(first_signal_components):
            self.layout.addWidget(widget, index, 0)

        for index, widget in enumerate(second_signal_components):
            self.layout.addWidget(widget, index, 1)

        self.first_amplitude.hide()
        self.first_amplitude_text.hide()
        self.first_frequency.hide()
        self.first_frequency_text.hide()
        self.first_fullfilment.hide()
        self.first_fullfilment_text.hide()
        self.first_sample_rate.hide()
        self.first_sample_rate_text.hide()

        self.second_amplitude.hide()
        self.second_amplitude_text.hide()
        self.second_frequency.hide()
        self.second_frequency_text.hide()
        self.second_fullfilment.hide()
        self.second_fullfilment_text.hide()
        self.second_sample_rate.hide()
        self.second_sample_rate_text.hide()

    def show_first_signal_fields(self, index):
        if index == 0:
            self.first_amplitude.hide()
            self.first_amplitude_text.hide()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.hide()
            self.first_fullfilment_text.hide()
            self.first_sample_rate.hide()
            self.first_sample_rate_text.hide()
            self.first_signal_type = generate_gauss_noise
        elif index == 1:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.hide()
            self.first_fullfilment_text.hide()
            self.first_sample_rate.hide()
            self.first_sample_rate_text.hide()
            self.first_signal_type = generate_uniform_noise
        elif index == 2 or index == 3 or index == 4:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.show()
            self.first_frequency_text.show()
            self.first_fullfilment.hide()
            self.first_fullfilment_text.hide()
            self.first_sample_rate.hide()
            self.first_sample_rate_text.hide()
            if index == 2:
                self.first_signal_type = generate_sinusoidal_signal
            elif index == 3:
                self.first_signal_type = generate_sinusoidal_signal_one_half_straight
            elif index == 4:
                self.first_signal_type = generate_sinusoidal_signal_straight
        elif index == 5 or index == 6 or index == 7:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.show()
            self.first_frequency_text.show()
            self.first_fullfilment.show()
            self.first_fullfilment_text.setText("Długość okresu")
            self.first_fullfilment_text.show()
            self.first_sample_rate.hide()
            self.first_sample_rate_text.hide()
            if index == 5:
                self.first_signal_type = generate_rectangle_signal
            elif index == 6:
                self.first_signal_type = generate_rectangle_signal_symmetric
            elif index == 7:
                self.first_signal_type = generate_triangle_signal
        elif index == 8:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.show()
            self.first_fullfilment_text.setText("Czas skoku")
            self.first_fullfilment_text.show()
            self.first_sample_rate.hide()
            self.first_sample_rate_text.hide()
            self.first_signal_type = generate_unit_jump_signal
        elif index == 9 or index == 10:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.show()
            if index == 9:
                self.first_fullfilment_text.setText("Number próbki ze skokiem")
                self.first_signal_type = generate_unit_impulse
            else:
                self.first_fullfilment_text.setText("Prawdopodobieństwo skoku")
                self.first_signal_type = generate_impulse_noise

            self.first_fullfilment_text.show()
            self.first_sample_rate.show()
            self.first_sample_rate_text.show()

    def show_second_singal_fields(self, index):
        if index == 0:
            self.second_amplitude.hide()
            self.second_amplitude_text.hide()
            self.second_frequency.hide()
            self.second_frequency_text.hide()
            self.second_fullfilment.hide()
            self.second_fullfilment_text.hide()
            self.second_sample_rate.hide()
            self.second_sample_rate_text.hide()
        elif index == 1:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.hide()
            self.second_frequency_text.hide()
            self.second_fullfilment.hide()
            self.second_fullfilment_text.hide()
            self.second_sample_rate.hide()
            self.second_sample_rate_text.hide()
        elif index == 2 or index == 3 or index == 4:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.show()
            self.second_frequency_text.show()
            self.second_fullfilment.hide()
            self.second_fullfilment_text.hide()
            self.second_sample_rate.hide()
            self.second_sample_rate_text.hide()
        elif index == 5 or index == 6 or index == 7:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.show()
            self.second_frequency_text.show()
            self.second_fullfilment.show()
            self.second_fullfilment_text.setText("Długość okresu")
            self.second_fullfilment_text.show()
            self.second_sample_rate.hide()
            self.second_sample_rate_text.hide()
        elif index == 8:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.hide()
            self.second_frequency_text.hide()
            self.second_fullfilment.show()
            self.second_fullfilment_text.setText("Czas skoku")
            self.second_fullfilment_text.show()
            self.second_sample_rate.hide()
            self.second_sample_rate_text.hide()
        elif index == 9 or index == 10:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.show()
            if index == 9:
                self.second_fullfilment_text.setText("Number próbki ze skokiem")
            else:
                self.second_fullfilment_text.setText("Prawdopodobieństwo skoku")

            self.second_fullfilment_text.show()
            self.second_sample_rate.show()
            self.second_sample_rate_text.show()

    def generate_first_signal(self):
        signal = self.signal_factory.create(
            amplitude=self.first_amplitude.value(),
            signal_start_time=self.first_signal_start.value(),
            signal_duration=self.first_signal_length.value(),
            frequency=self.first_frequency.value(),
            type_of_signal=self.first_signal_type,
            fullfilment=self.first_fullfilment.value(),
            sample_rate=self.first_sample_rate.value(),
        )
        if self.first_signal.currentIndex() == 9 or self.first_signal.currentIndex() == 10:
            plot_discrete(signal)
        else:
            plot_continuous(signal)
