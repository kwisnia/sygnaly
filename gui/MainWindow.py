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
