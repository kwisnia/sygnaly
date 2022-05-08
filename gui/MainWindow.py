from PySide6 import QtWidgets, QtCore
from gui.SignalStatsWindow import SignalStatsWindow
from plot import histogram, plot_continuous, plot_discrete
from SignalFactory import SignalFactory
from functions import *
from operations import *
from quantization import quantize_rounded
from reconstruction import first_order_hold, sinc, zero_order_hold
from stats import mean_square_error
from copy import deepcopy


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
        self.reconstruction_methods = [
            "Zero order hold",
            "First order hold",
            "Interpolacja sinc",
        ]

        self.first_signal_combobox = QtWidgets.QComboBox()
        self.first_signal_reconstruction_combobox = QtWidgets.QComboBox()
        self.first_signal_type = generate_gauss_noise
        self.second_signal_type = generate_gauss_noise
        self.first_signal = None
        self.second_signal = None
        self.first_signal_combobox.addItems(self.signals)
        self.first_signal_reconstruction_combobox.addItems(self.reconstruction_methods)
        self.second_signal_combobox = QtWidgets.QComboBox()
        self.second_signal_reconstruction_combobox = QtWidgets.QComboBox()
        self.operation_result_reconstruction_combobox = QtWidgets.QComboBox()
        self.operation_result_reconstruction_combobox.addItems(
            self.reconstruction_methods
        )
        self.second_signal_combobox.addItems(self.signals)
        self.second_signal_reconstruction_combobox.addItems(self.reconstruction_methods)
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
        self.operation_result_sample_rate = QtWidgets.QDoubleSpinBox()
        self.first_bit_count = QtWidgets.QDoubleSpinBox()
        self.second_bit_count = QtWidgets.QDoubleSpinBox()
        self.operation_result_bit_count = QtWidgets.QDoubleSpinBox()
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
        self.first_bit_count_text = QtWidgets.QLabel("Liczba bitów kwantyfikacji")
        self.second_bit_count_text = QtWidgets.QLabel("Liczba bitów kwantyfikacji")
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
        self.first_frequency.setMaximum(100000)
        self.second_frequency.setMaximum(100000)
        self.first_fullfilment.setMaximum(10000)
        self.second_fullfilment.setMaximum(10000)
        self.first_sample_rate.setMaximum(100000)
        self.second_sample_rate.setMaximum(100000)

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
        self.operation_result_sample_rate_text = QtWidgets.QLabel(
            "Częstotliwość próbkowania"
        )
        self.operation_result_bit_count_text = QtWidgets.QLabel(
            "Liczba bitów kwantyfikacji"
        )
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
            self.first_bit_count_text,
            self.first_bit_count,
            QtWidgets.QLabel("Typ rekonstrukcji pierwszego sygnału"),
            self.first_signal_reconstruction_combobox,
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
            self.second_bit_count_text,
            self.second_bit_count,
            QtWidgets.QLabel("Typ rekonstrukcji drugiego sygnału"),
            self.second_signal_reconstruction_combobox,
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

        self.layout.addWidget(self.operation_result_bit_count_text, 22, 0, 2, 2)
        self.layout.addWidget(self.operation_result_bit_count, 23, 0, 2, 2)
        self.layout.addWidget(self.operation_result_sample_rate_text, 24, 0, 2, 2)
        self.layout.addWidget(self.operation_result_sample_rate, 25, 0, 2, 2)
        self.layout.addWidget(
            self.operation_result_reconstruction_combobox, 26, 0, 2, 2
        )
        self.layout.addWidget(self.add_signals_button, 27, 0, 2, 2)
        self.layout.addWidget(self.substract_signals_button, 28, 0, 2, 2)
        self.layout.addWidget(self.multiply_signals_button, 29, 0, 2, 2)
        self.layout.addWidget(self.divide_signals_button, 30, 0, 2, 2)
        self.layout.addWidget(self.operation_signal_file_name, 31, 0, 2, 2)
        self.layout.addWidget(self.operation_signal_save_button, 32, 0, 2, 2)

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

    def plot_signal(self, signal: Signal, second_signal: Signal = None):
        plot_discrete(signal, second_signal)
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
        signal2 = self.signal_factory.create(
            amplitude=self.first_amplitude.value(),
            signal_start_time=self.first_signal_start.value(),
            signal_duration=self.first_signal_length.value(),
            frequency=self.first_frequency.value(),
            sample_rate=10000,
            type_of_signal=self.first_signal_type,
            fullfilment=self.first_fullfilment.value(),
        )
        self.first_signal = signal2
        return signal, signal2

    def generate_first_and_plot(self):
        sampled_signal, original_signal = self.generate_first_signal()
        self.plot_signal(sampled_signal, original_signal)
        quantized_signal = quantize_rounded(
            sampled_signal, int(self.first_bit_count.value()), original_signal
        )
        index = self.first_signal_reconstruction_combobox.currentIndex()
        if index == 0:
            reconstructed_signal = zero_order_hold(sampled_signal, original_signal)
        elif index == 1:
            reconstructed_signal = first_order_hold(sampled_signal, original_signal)
        else:
            reconstructed_signal = sinc(sampled_signal, original_signal)
        self.first_signal = reconstructed_signal
        self.popup = SignalStatsWindow(
            original_signal, reconstructed_signal, sampled_signal, quantized_signal
        )
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
        self.second_signal = self.signal_factory.create(
            amplitude=self.second_amplitude.value(),
            signal_start_time=self.second_signal_start.value(),
            signal_duration=self.second_signal_length.value(),
            frequency=self.second_frequency.value(),
            sample_rate=10000,
            type_of_signal=self.second_signal_type,
            fullfilment=self.second_fullfilment.value(),
        )
        signal2 = self.second_signal
        return signal, signal2

    def generate_second_and_plot(self):
        sampled_signal, original_signal = self.generate_second_signal()
        self.plot_signal(sampled_signal, original_signal)
        quantized_signal = quantize_rounded(
            sampled_signal, int(self.first_bit_count.value()), original_signal
        )
        index = self.second_signal_reconstruction_combobox.currentIndex()
        if index == 0:
            reconstructed_signal = zero_order_hold(sampled_signal, original_signal)
        elif index == 1:
            reconstructed_signal = first_order_hold(sampled_signal, original_signal)
        else:
            reconstructed_signal = sinc(sampled_signal, original_signal)
        self.second_signal = reconstructed_signal
        self.popup = SignalStatsWindow(
            original_signal, reconstructed_signal, sampled_signal, quantized_signal
        )
        self.popup.show()

    def save_first_signal_to_file(self):
        save_to_file(self.generate_first_signal(), self.first_signal_file_name.text())

    def save_second_signal_to_file(self):
        save_to_file(self.generate_second_signal(), self.second_signal_file_name.text())

    def sample_operation_result(self):

        # sample_step = int(
        #     10000
        #     // self.operation_result.signal_duration
        #     // self.operation_result_bit_count.value()
        # )

        sampled_signal = deepcopy(self.operation_result)
        sampled_signal.samples = np.linspace(
            self.operation_result.signal_start_time,
            self.operation_result.signal_start_time
            + self.operation_result.signal_duration,
            int(
                self.operation_result.signal_duration
                * self.operation_result_sample_rate.value()
            ),
        )
        sampled_signal.values = []
        for x in sampled_signal.samples:
            desired_index = np.searchsorted(self.operation_result.samples, x)
            sampled_signal.values.append(self.operation_result.values[desired_index])
        sampled_signal.values = np.array(sampled_signal.values)
        sampled_signal.sample_rate = self.operation_result_sample_rate.value()
        # sampled_signal.values = self.operation_result.values[::sample_step]
        return sampled_signal

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
        sampled_signal = self.sample_operation_result()
        self.plot_signal(sampled_signal, self.operation_result)
        quantized_signal = quantize_rounded(
            sampled_signal,
            int(self.operation_result_bit_count.value()),
            self.operation_result,
        )
        index = self.operation_result_reconstruction_combobox.currentIndex()
        if index == 0:
            reconstructed_signal = zero_order_hold(
                sampled_signal, self.operation_result
            )
        elif index == 1:
            reconstructed_signal = first_order_hold(
                sampled_signal, self.operation_result
            )
        else:
            reconstructed_signal = sinc(sampled_signal, self.operation_result)
        self.popup = SignalStatsWindow(
            self.operation_result,
            reconstructed_signal,
            sampled_signal,
            quantized_signal,
        )
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
        sampled_signal = self.sample_operation_result()
        self.plot_signal(sampled_signal, self.operation_result)
        quantized_signal = quantize_rounded(
            sampled_signal,
            int(self.operation_result_bit_count.value()),
            self.operation_result,
        )
        index = self.operation_result_reconstruction_combobox.currentIndex()
        if index == 0:
            reconstructed_signal = zero_order_hold(
                sampled_signal, self.operation_result
            )
        elif index == 1:
            reconstructed_signal = first_order_hold(
                sampled_signal, self.operation_result
            )
        else:
            reconstructed_signal = sinc(sampled_signal, self.operation_result)
        self.popup = SignalStatsWindow(
            self.operation_result,
            reconstructed_signal,
            sampled_signal,
            quantized_signal,
        )
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
        sampled_signal = self.sample_operation_result()
        self.plot_signal(sampled_signal, self.operation_result)
        quantized_signal = quantize_rounded(
            sampled_signal,
            int(self.operation_result_bit_count.value()),
            self.operation_result,
        )
        index = self.operation_result_reconstruction_combobox.currentIndex()
        if index == 0:
            reconstructed_signal = zero_order_hold(
                sampled_signal, self.operation_result
            )
        elif index == 1:
            reconstructed_signal = first_order_hold(
                sampled_signal, self.operation_result
            )
        else:
            reconstructed_signal = sinc(sampled_signal, self.operation_result)
        self.popup = SignalStatsWindow(
            self.operation_result,
            reconstructed_signal,
            sampled_signal,
            quantized_signal,
        )
        self.popup.show()

    def divide_signals(self):
        if self.first_signal is None:
            self.generate_first_signal()
        if self.second_signal is None:
            self.generate_second_signal()
        self.operation_signal_file_name.show()
        self.operation_signal_save_button.show()
        self.operation_result = divide(self.first_signal, self.second_signal)
        sampled_signal = self.sample_operation_result()
        self.plot_signal(sampled_signal, self.operation_result)
        quantized_signal = quantize_rounded(
            sampled_signal,
            int(self.operation_result_bit_count.value()),
            self.operation_result,
        )
        index = self.operation_result_reconstruction_combobox.currentIndex()
        if index == 0:
            reconstructed_signal = zero_order_hold(
                sampled_signal, self.operation_result
            )
        elif index == 1:
            reconstructed_signal = first_order_hold(
                sampled_signal, self.operation_result
            )
        else:
            reconstructed_signal = sinc(sampled_signal, self.operation_result)
        self.popup = SignalStatsWindow(
            self.operation_result,
            reconstructed_signal,
            sampled_signal,
            quantized_signal,
        )
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
        self.plot_signal(self.second_signal)
