from PySide6 import QtWidgets, QtCore
from gui.SignalStatsWindow import SignalStatsWindow
from plot import histogram, plot_continuous, plot_discrete
from SignalFactory import SignalFactory
from functions import *
from operations import *


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.signal_factory = SignalFactory()

        self.signals = [
            "Szum gaussowski",
            "Szum o rozkładzie jednostajnym",
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

        self.first_signal_combobox = QtWidgets.QComboBox()
        self.first_signal_type = generate_gauss_noise
        self.second_signal_type = generate_gauss_noise
        self.first_signal = None
        self.second_signal = None
        self.first_signal_combobox.addItems(self.signals)
        self.second_signal_combobox = QtWidgets.QComboBox()
        self.second_signal_combobox.addItems(self.signals)
        self.first_signal_combobox.currentIndexChanged.connect(
            self.show_first_signal_fields
        )
        self.second_signal_combobox.currentIndexChanged.connect(
            self.show_second_signal_fields
        )
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
        self.first_signal_file_name = QtWidgets.QLineEdit("Nazwa pliku")
        self.second_signal_file_name = QtWidgets.QLineEdit("Nazwa pliku")
        self.operation_signal_file_name = QtWidgets.QLineEdit("Nazwa pliku")
        self.first_signal_save_button = QtWidgets.QPushButton("Zapisz sygnał do pliku")
        self.first_signal_load_button = QtWidgets.QPushButton("Wczytaj sygnał z pliku")
        self.second_signal_save_button = QtWidgets.QPushButton("Zapisz sygnał do pliku")
        self.second_signal_load_button = QtWidgets.QPushButton("Wczytaj sygnał z pliku")
        self.operation_signal_save_button = QtWidgets.QPushButton(
            "Zapisz sygnał z ostatniej operacji do pliku"
        )

        self.first_signal_start.setMaximum(10000)
        self.second_signal_start.setMaximum(10000)
        self.first_signal_length.setMaximum(10000)
        self.second_signal_length.setMaximum(10000)
        self.first_amplitude.setMaximum(10000)
        self.second_amplitude.setMaximum(10000)
        self.first_frequency.setMaximum(10000)
        self.second_frequency.setMaximum(10000)
        self.first_fullfilment.setMaximum(10000)
        self.second_fullfilment.setMaximum(10000)
        self.first_sample_rate.setMaximum(10000)
        self.second_sample_rate.setMaximum(10000)

        self.first_signal_generate.clicked.connect(self.generate_first_and_plot)
        self.second_signal_generate.clicked.connect(self.generate_second_and_plot)

        self.first_signal_save_button.clicked.connect(self.save_first_signal_to_file)
        self.second_signal_save_button.clicked.connect(self.save_second_signal_to_file)

        self.first_signal_load_button.clicked.connect(self.load_first_signal)
        self.second_signal_load_button.clicked.connect(self.load_second_signal)

        self.add_signals_button = QtWidgets.QPushButton("Dodaj sygnały")
        self.substract_signals_button = QtWidgets.QPushButton("Odejmij sygnały")
        self.multiply_signals_button = QtWidgets.QPushButton("Pomnóż sygnały")
        self.divide_signals_button = QtWidgets.QPushButton("Podziel sygnały")

        self.add_signals_button.clicked.connect(self.add_signals)
        self.substract_signals_button.clicked.connect(self.substract_signals)
        self.multiply_signals_button.clicked.connect(self.multiply_signals)
        self.divide_signals_button.clicked.connect(self.divide_signals)
        self.operation_signal_save_button.clicked.connect(
            self.save_operation_signal_to_file
        )

        first_signal_components = [
            QtWidgets.QLabel("Typ pierwszego sygnału"),
            self.first_signal_combobox,
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
            self.first_signal_file_name,
            self.first_signal_save_button,
            self.first_signal_load_button,
        ]

        second_signal_components = [
            QtWidgets.QLabel("Typ drugiego sygnału"),
            self.second_signal_combobox,
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
            self.second_signal_file_name,
            self.second_signal_save_button,
            self.second_signal_load_button,
        ]

        self.layout = QtWidgets.QGridLayout(self)

        for index, widget in enumerate(first_signal_components):
            self.layout.addWidget(widget, index, 0)

        for index, widget in enumerate(second_signal_components):
            self.layout.addWidget(widget, index, 1)

        self.layout.addWidget(self.add_signals_button, 18, 0, 2, 2)
        self.layout.addWidget(self.substract_signals_button, 19, 0, 2, 2)
        self.layout.addWidget(self.multiply_signals_button, 20, 0, 2, 2)
        self.layout.addWidget(self.divide_signals_button, 21, 0, 2, 2)
        self.layout.addWidget(self.operation_signal_file_name, 22, 0, 2, 2)
        self.layout.addWidget(self.operation_signal_save_button, 23, 0, 2, 2)

        self.first_amplitude.hide()
        self.first_amplitude_text.hide()
        self.first_frequency.hide()
        self.first_frequency_text.hide()
        self.first_fullfilment.hide()
        self.first_fullfilment_text.hide()

        self.second_amplitude.hide()
        self.second_amplitude_text.hide()
        self.second_frequency.hide()
        self.second_frequency_text.hide()
        self.second_fullfilment.hide()
        self.second_fullfilment_text.hide()

        self.operation_signal_file_name.hide()
        self.operation_signal_save_button.hide()

    def show_first_signal_fields(self, index):
        if index == 0:
            self.first_amplitude.hide()
            self.first_amplitude_text.hide()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.hide()
            self.first_fullfilment_text.hide()
            self.first_signal_type = generate_gauss_noise
        elif index == 1:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.hide()
            self.first_fullfilment_text.hide()
            self.first_signal_type = generate_uniform_noise
        elif index == 2 or index == 3 or index == 4:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.show()
            self.first_frequency_text.show()
            self.first_fullfilment.hide()
            self.first_fullfilment_text.hide()
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
            self.first_fullfilment_text.setText("Współczynnik wypełnienia")
            self.first_fullfilment_text.show()
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

    def show_second_signal_fields(self, index):
        if index == 0:
            self.second_amplitude.hide()
            self.second_amplitude_text.hide()
            self.second_frequency.hide()
            self.second_frequency_text.hide()
            self.second_fullfilment.hide()
            self.second_fullfilment_text.hide()
            self.second_signal_type = generate_gauss_noise
        elif index == 1:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.hide()
            self.second_frequency_text.hide()
            self.second_fullfilment.hide()
            self.second_fullfilment_text.hide()
            self.second_signal_type = generate_uniform_noise
        elif index == 2 or index == 3 or index == 4:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.show()
            self.second_frequency_text.show()
            self.second_fullfilment.hide()
            self.second_fullfilment_text.hide()
            if index == 2:
                self.second_signal_type = generate_sinusoidal_signal
            elif index == 3:
                self.second_signal_type = generate_sinusoidal_signal_one_half_straight
            elif index == 4:
                self.second_signal_type = generate_sinusoidal_signal_straight
        elif index == 5 or index == 6 or index == 7:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.show()
            self.second_frequency_text.show()
            self.second_fullfilment.show()
            self.second_fullfilment_text.setText("Długość okresu")
            self.second_fullfilment_text.show()
            if index == 5:
                self.second_signal_type = generate_rectangle_signal
            elif index == 6:
                self.second_signal_type = generate_rectangle_signal_symmetric
            elif index == 7:
                self.second_signal_type = generate_triangle_signal
        elif index == 8:
            self.second_amplitude_text.show()
            self.second_amplitude.show()
            self.second_frequency.hide()
            self.second_frequency_text.hide()
            self.second_fullfilment.show()
            self.second_fullfilment_text.setText("Czas skoku")
            self.second_fullfilment_text.show()
            self.second_signal_type = generate_unit_jump_signal
        elif index == 9 or index == 10:
            self.first_amplitude_text.show()
            self.first_amplitude.show()
            self.first_frequency.hide()
            self.first_frequency_text.hide()
            self.first_fullfilment.show()
            if index == 9:
                self.second_fullfilment_text.setText("Number próbki ze skokiem")
                self.second_signal_type = generate_unit_impulse
            else:
                self.second_fullfilment_text.setText("Prawdopodobieństwo skoku")
                self.second_signal_type = generate_impulse_noise

            self.second_fullfilment_text.show()
            self.second_sample_rate.show()
            self.second_sample_rate_text.show()

    def plot_signal(self, signal: Signal, combobox: QtWidgets.QComboBox):
        if combobox.currentIndex() == 9 or combobox.currentIndex() == 10:
            plot_discrete(signal)
        else:
            plot_continuous(signal)
        histogram(signal, int(signal.signal_duration))

    def generate_first_signal(self):
        signal = self.signal_factory.create(
            amplitude=self.first_amplitude.value(),
            signal_start_time=self.first_signal_start.value(),
            signal_duration=self.first_signal_length.value(),
            frequency=self.first_frequency.value(),
            sample_rate=self.first_sample_rate.value(),
            type_of_signal=self.first_signal_type,
            fullfilment=self.first_fullfilment.value(),
        )
        self.first_signal = signal
        return signal

    def generate_first_and_plot(self):
        signal = self.generate_first_signal()
        self.plot_signal(signal, self.first_signal_combobox)
        self.popup = SignalStatsWindow(signal)
        self.popup.show()

    def generate_second_signal(self):
        signal = self.signal_factory.create(
            amplitude=self.second_amplitude.value(),
            signal_start_time=self.second_signal_start.value(),
            signal_duration=self.second_signal_length.value(),
            frequency=self.second_frequency.value(),
            sample_rate=self.second_sample_rate.value(),
            type_of_signal=self.second_signal_type,
            fullfilment=self.second_fullfilment.value(),
        )
        self.second_signal = signal
        return signal

    def generate_second_and_plot(self):
        signal = self.generate_second_signal()
        self.plot_signal(signal, self.second_signal_combobox)
        self.popup = SignalStatsWindow(signal)
        self.popup.show()

    def save_first_signal_to_file(self):
        save_to_file(self.generate_first_signal(), self.first_signal_file_name.text())

    def save_second_signal_to_file(self):
        save_to_file(self.generate_second_signal(), self.second_signal_file_name.text())

    def add_signals(self):
        if self.first_signal is None:
            self.generate_first_signal()
        if self.second_signal is None:
            self.generate_second_signal()
        self.operation_signal_file_name.show()
        self.operation_signal_save_button.show()
        self.operation_result = add(
            self.first_signal,
            self.second_signal,
        )

        self.plot_signal(self.operation_result, self.first_signal_combobox)
        self.popup = SignalStatsWindow(self.operation_result)
        self.popup.show()

    def substract_signals(self):
        if self.first_signal is None:
            self.generate_first_signal()
        if self.second_signal is None:
            self.generate_second_signal()
        self.operation_signal_file_name.show()
        self.operation_signal_save_button.show()
        self.operation_result = subtract(
            self.first_signal,
            self.second_signal,
        )
        self.plot_signal(self.operation_result, self.first_signal_combobox)
        self.popup = SignalStatsWindow(self.operation_result)
        self.popup.show()

    def multiply_signals(self):
        if self.first_signal is None:
            self.generate_first_signal()
        if self.second_signal is None:
            self.generate_second_signal()
        self.operation_signal_file_name.show()
        self.operation_signal_save_button.show()
        self.operation_result = multiply(
            self.first_signal,
            self.second_signal,
        )
        self.plot_signal(self.operation_result, self.first_signal_combobox)
        self.popup = SignalStatsWindow(self.operation_result)
        self.popup.show()

    def divide_signals(self):
        if self.first_signal is None:
            self.generate_first_signal()
        if self.second_signal is None:
            self.generate_second_signal()
        self.operation_signal_file_name.show()
        self.operation_signal_save_button.show()
        self.operation_result = divide(self.first_signal, self.second_signal)
        self.plot_signal(self.operation_result, self.first_signal_combobox)
        self.popup = SignalStatsWindow(self.operation_result)
        self.popup.show()

    def save_operation_signal_to_file(self):
        save_to_file(self.operation_result, self.operation_signal_file_name.text())

    def load_first_signal(
        self,
    ):
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Wybierz sygnał", ".", "Pliki JSON (*.json)"
        )
        self.first_signal = load_from_file(fileName[0])
        self.plot_signal(self.first_signal, self.first_signal_combobox)

    def load_second_signal(
        self,
    ):
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Wybierz sygnał", ".", "Pliki JSON (*.json)"
        )
        print(fileName)
        self.second_signal = load_from_file(fileName[0])
        self.plot_signal(self.second_signal, self.second_signal_combobox)
