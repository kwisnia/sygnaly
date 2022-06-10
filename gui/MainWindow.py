from copy import deepcopy
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from SignalFactory import SignalFactory
from filters import high_pass_filter, low_pass_filter
from functions import *
from gui.SimulatorWindow import SimulatorWindow
from stats import *
from gui.SignalTypes import SignalTypes
from gui.custom_widgets.PlotTypes import PlotTypes
from gui.custom_widgets.PlotWidget import PlotWidget
from gui.ui_mainwindow import Ui_MainWindow
from operations import add, convolve, corelate, divide, multiply, subtract
from quantization import quantize_rounded
from reconstruction import first_order_hold, sinc, zero_order_hold
from transformations import (
    dft,
    dit_fft,
    fast_cosine_transform,
    inverse_dft,
    inverse_fast_cosine_transform,
    inverse_dit_fft,
    walsh_hadamard_transform,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signal_factory = SignalFactory()
        self.signal_types = [
            generate_gauss_noise,
            generate_uniform_noise,
            generate_sinusoidal_signal,
            generate_sinusoidal_signal_one_half_straight,
            generate_sinusoidal_signal_straight,
            generate_rectangle_signal,
            generate_rectangle_signal_symmetric,
            generate_triangle_signal,
            generate_unit_jump_signal,
            generate_unit_impulse,
            generate_impulse_noise,
            low_pass_filter,
            high_pass_filter,
        ]
        self.multi_argument_operations = [
            add,
            subtract,
            multiply,
            divide,
            convolve,
            corelate,
        ]
        self.reconstruction_types = [
            zero_order_hold,
            first_order_hold,
            sinc,
        ]
        self.leftGraphWidget = PlotWidget()
        self.leftHistWidget = PlotWidget()
        self.rightGraphWidget = PlotWidget()
        self.rightHistWidget = PlotWidget()
        self.resultGraphWidget = PlotWidget(560, 380)
        self.resultHistWidget = PlotWidget(560, 380)
        self.w1UpperPlotWidget = PlotWidget(560, 220)
        self.w1LowerPlotWidget = PlotWidget(560, 220)
        self.w2UpperPlotWidget = PlotWidget(560, 220)
        self.w2LowerPlotWidget = PlotWidget(560, 220)

        self.left_signal = None
        self.right_signal = None
        self.operation_result = None

        self.ui.wykresLewyLayout.addChildWidget(self.leftGraphWidget)
        self.ui.histogramLewyLayout.addChildWidget(self.leftHistWidget)
        self.ui.wykresPrawyLayout.addChildWidget(self.rightGraphWidget)
        self.ui.histogramPrawyLayout.addChildWidget(self.rightHistWidget)
        self.ui.wykresWynikowyLayout.addChildWidget(self.resultGraphWidget)
        self.ui.histogramWynikowyLayout.addChildWidget(self.resultHistWidget)
        self.ui.wykresW1LayoutUpper.addChildWidget(self.w1UpperPlotWidget)
        self.ui.wykresW1LayoutLower.addChildWidget(self.w1LowerPlotWidget)
        self.ui.wykresW2LayoutUpper.addChildWidget(self.w2UpperPlotWidget)
        self.ui.wykresW2LayoutLower.addChildWidget(self.w2LowerPlotWidget)
        self.ui.generujLewy.clicked.connect(lambda: self.generate_signal())
        self.ui.generujPrawy.clicked.connect(
            lambda: self.generate_signal(second_signal=True)
        )
        self.ui.zapiszButton.clicked.connect(self.save_to_file)
        self.ui.wczytajButton.clicked.connect(self.load_from_file)
        self.ui.dzialaniaJednoWykonajButton.clicked.connect(
            self.single_argument_operation
        )
        self.ui.dzialaniaDwuWykonajButton.clicked.connect(self.multi_argument_operation)
        self.ui.actiondystans.triggered.connect(self.open_simulator_window)

    def _get_value(self, widget_name):
        try:
            spinbox = getattr(self.ui, widget_name)
        except AttributeError:
            return None
        return spinbox.value()

    def _get_combobox_value(self, widget_name):
        try:
            combobox = getattr(self.ui, widget_name)
        except AttributeError:
            return None
        return combobox.currentIndex()

    def _get_signal_from_combobox(self, combobox_name):
        combobox_index = self._get_combobox_value(combobox_name)
        if combobox_index == 0:
            return SignalTypes.LEFT, self.left_signal
        elif combobox_index == 1:
            return SignalTypes.RIGHT, self.right_signal
        else:
            return SignalTypes.MIXED, self.operation_result

    def _get_plot_type_from_index(self, signal_index):
        if signal_index == 10 or signal_index == 11:
            return PlotTypes.SCATTER
        elif signal_index == 12 or signal_index == 13:
            return PlotTypes.STEM
        return PlotTypes.LINE

    def _get_plot_type_from_name(self, signal_name):
        if signal_name == "unitimpulse" or signal_name == "impulsenoise":
            return PlotTypes.SCATTER
        elif signal_name == "lowpassfilter" or signal_name == "highpassfilter":
            return PlotTypes.STEM
        return PlotTypes.LINE

    def _plot_signal(
        self, signal_type: SignalTypes, signal: Signal, plot_type: PlotTypes
    ):
        if signal_type == SignalTypes.LEFT:
            self.leftGraphWidget.plot(signal.samples, signal.values, plot_type)
            self.leftHistWidget.plot(signal.samples, signal.values, PlotTypes.HISTOGRAM)
        elif signal_type == SignalTypes.RIGHT:
            self.rightGraphWidget.plot(signal.samples, signal.values, plot_type)
            self.rightHistWidget.plot(
                signal.samples, signal.values, PlotTypes.HISTOGRAM
            )
        else:
            self.resultGraphWidget.plot(signal.samples, signal.values, plot_type)
            self.resultHistWidget.plot(
                signal.samples, signal.values, PlotTypes.HISTOGRAM
            )

    def _fill_stats_tab(
        self, signal_type: SignalTypes, signal: Signal, second_signal: Signal = None
    ):
        stat_table = self.ui.statystykiLewyWidget
        if signal_type == SignalTypes.RIGHT:
            stat_table = self.ui.statystykiPrawyWidget
        elif signal_type == SignalTypes.MIXED:
            stat_table = self.ui.statystykiWynikowyWidget

        stats = [
            avg_signal_value,
            abs_avg_signal_value,
            avg_signal_power,
            variance_signal_value,
            rms_signal_value,
        ]
        stats_extra = [
            mean_square_error,
            signal_to_noise_ratio,
            peak_signal_to_noise_ratio,
            maximum_difference,
        ]
        for row in range(stat_table.rowCount()):
            stat_table.item(row, 0).setText(str(round(stats[row](signal), 5)))
        if second_signal is not None:
            for row in range(self.ui.statystykiWynikowyExtraWidget.rowCount()):
                self.ui.statystykiWynikowyExtraWidget.item(row, 0).setText(
                    str(round(stats_extra[row](second_signal, signal), 5))
                )

    def open_simulator_window(self):
        self.simulator_window = SimulatorWindow()
        self.simulator_window.show()

    def sample_signal(self, signal_to_sample: Signal):
        sampled_signal = deepcopy(signal_to_sample)
        sampled_signal.samples = np.linspace(
            signal_to_sample.signal_start_time,
            signal_to_sample.signal_start_time + signal_to_sample.signal_duration,
            int(
                signal_to_sample.signal_duration
                * self.ui.jednoCzestotliwoscProbkowaniaDoubleSpinBox.value()
            ),
        )
        sampled_signal.values = []
        for x in sampled_signal.samples:
            desired_index = np.searchsorted(signal_to_sample.samples, x)
            sampled_signal.values.append(signal_to_sample.values[desired_index])
        sampled_signal.sample_rate = (
            self.ui.jednoCzestotliwoscProbkowaniaDoubleSpinBox.value()
        )
        sampled_signal.name = "sampled"
        self.sampled_signal = sampled_signal
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            sampled_signal.samples, sampled_signal.values, PlotTypes.STEM, False
        )
        self.resultGraphWidget.plot(
            signal_to_sample.samples, signal_to_sample.values, PlotTypes.LINE, False
        )
        self.resultHistWidget.plot(
            sampled_signal.samples, sampled_signal.values, PlotTypes.HISTOGRAM
        )

        return sampled_signal

    def quantize_signal(self, signal_to_quantize: Signal):
        quantized_signal = quantize_rounded(
            self.sampled_signal,
            int(self.ui.bityKwantyzacjiDoubleSpinBox.value()),
        )
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            quantized_signal.samples, quantized_signal.values, PlotTypes.STEM, False
        )
        self.resultGraphWidget.plot(
            signal_to_quantize.samples, signal_to_quantize.values, PlotTypes.LINE, False
        )
        return quantized_signal

    def reconstruct_signal(self, signal_to_reconstruct: Signal):
        reconstructed_signal = self.reconstruction_types[
            self.ui.typRekonstrukcjiComboBox.currentIndex()
        ](self.sampled_signal, signal_to_reconstruct)
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            reconstructed_signal.samples,
            reconstructed_signal.values,
            PlotTypes.LINE,
            False,
        )
        self.resultHistWidget.plot(
            reconstructed_signal.samples,
            reconstructed_signal.values,
            PlotTypes.HISTOGRAM,
        )
        self.resultGraphWidget.plot(
            signal_to_reconstruct.samples,
            reconstructed_signal.values,
            PlotTypes.LINE,
            False,
        )
        return reconstructed_signal

    def transform_signal_cosine(self, signal_to_transform: Signal):
        transformed_signal = fast_cosine_transform(signal_to_transform)
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            transformed_signal.samples,
            transformed_signal.values,
            PlotTypes.LINE,
            False,
        )
        return transformed_signal

    def transform_signal_icosine(self, signal_to_transform: Signal):
        transformed_signal = inverse_fast_cosine_transform(signal_to_transform)
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            transformed_signal.samples,
            transformed_signal.values,
            PlotTypes.LINE,
            False,
        )
        return transformed_signal

    def transform_signal_wht(self, signal_to_transform: Signal):
        transformed_signal = walsh_hadamard_transform(signal_to_transform)
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            transformed_signal.samples,
            transformed_signal.values,
            PlotTypes.LINE,
            False,
        )
        return transformed_signal

    def transform_signal_wht_inverse(self, signal_to_transform: Signal):
        transformed_signal = walsh_hadamard_transform(signal_to_transform, inverted=True)
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            transformed_signal.samples,
            transformed_signal.values,
            PlotTypes.LINE,
            False,
        )
        return transformed_signal

    def transform_signal_fft(self, signal_to_transform: Signal):
        return self.complex_transform(signal_to_transform, dit_fft)

    def transform_signal_ifft(self, signal_to_transform: Signal):
        return self.inverse_complex_transform(signal_to_transform, inverse_dit_fft)

    def transform_signal_dft(self, signal_to_transform: Signal):
        return self.complex_transform(signal_to_transform, dft)

    def transform_signal_idft(self, signal_to_transform: Signal):
        return self.inverse_complex_transform(signal_to_transform, inverse_dft)

    def inverse_complex_transform(
        self, signal_to_transform: Signal, transform_function
    ):
        transformed_signal = transform_function(signal_to_transform)
        self.resultGraphWidget.axes.clear()
        self.resultGraphWidget.plot(
            transformed_signal.samples,
            transformed_signal.values,
            PlotTypes.LINE,
            False,
        )
        return transformed_signal

    def complex_transform(self, signal_to_transform, transform_function):
        transformed_signal = transform_function(signal_to_transform)
        self.w1LowerPlotWidget.axes.clear()
        self.w1UpperPlotWidget.axes.clear()
        self.w2LowerPlotWidget.axes.clear()
        self.w2UpperPlotWidget.axes.clear()
        self.w1UpperPlotWidget.plot(
            transformed_signal.samples,
            [value.real for value in transformed_signal.values],
            PlotTypes.LINE,
            False,
        )
        self.w1LowerPlotWidget.plot(
            transformed_signal.samples,
            [value.imag for value in transformed_signal.values],
            PlotTypes.LINE,
            False,
        )
        self.w2UpperPlotWidget.plot(
            transformed_signal.samples,
            np.abs(transformed_signal.values),
            PlotTypes.LINE,
            False,
        )
        self.w2LowerPlotWidget.plot(
            transformed_signal.samples,
            np.angle(transformed_signal.values),
            PlotTypes.LINE,
            False,
        )
        return transformed_signal

    def generate_signal(self, second_signal=False):
        selected_signal_type = self.ui.typSygnaluComboBox.currentIndex() + 1
        generated_signal = self.signal_factory.create(
            self._get_value(f"amplitudaDoubleSpinBox_{selected_signal_type}"),
            self._get_value(f"poczatekSygnaluDoubleSpinBox_{selected_signal_type}"),
            self._get_value(f"dlugoscSygnaluDoubleSpinBox_{selected_signal_type}"),
            self._get_value(f"czestotliwoscDoubleSpinBox_{selected_signal_type}"),
            self._get_value(
                f"czestotliwoscProbkowaniaDoubleSpinBox_{selected_signal_type}"
            ),
            self.signal_types[selected_signal_type - 1],
            self._get_value(
                f"wspolczynnikWypelnieniaDoubleSpinBox_{selected_signal_type}"
            )
            if selected_signal_type != 12 and selected_signal_type != 13
            else self._get_combobox_value(f"typOknaComboBox_{selected_signal_type}"),
        )
        plot_type = self._get_plot_type_from_index(selected_signal_type)
        if second_signal:
            self.right_signal = generated_signal
            self._plot_signal(SignalTypes.RIGHT, generated_signal, plot_type)
            self._fill_stats_tab(SignalTypes.RIGHT, generated_signal)
        else:
            self.left_signal = generated_signal
            self._plot_signal(SignalTypes.LEFT, generated_signal, plot_type)
            self._fill_stats_tab(SignalTypes.LEFT, generated_signal)

    def save_to_file(self):
        signal_to_save = self._get_signal_from_combobox("zapiszDoPlikuComboBox")[1]
        filename = QtWidgets.QFileDialog.getSaveFileName(
            self, "Zapisz do pliku", ".", "Pliki JSON (*.json)"
        )
        save_to_file(signal_to_save, filename[0])

    def load_from_file(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Wybierz sygnał", ".", "Pliki JSON (*.json)"
        )
        signal_type, signal_to_load = self._get_signal_from_combobox(
            "wczytajZPlikuComboBox"
        )
        signal_to_load = load_from_file(fileName[0])
        plot_type = self._get_plot_type_from_name(signal_to_load.name)
        self._plot_signal(signal_type, signal_to_load, plot_type)

    def single_argument_operation(self):
        operation_type = self.ui.operacjaJednoComboBox.currentIndex()
        operation_types = [
            self.sample_signal,
            self.quantize_signal,
            self.reconstruct_signal,
            self.transform_signal_dft,
            self.transform_signal_idft,
            self.transform_signal_fft,
            self.transform_signal_ifft,
            self.transform_signal_cosine,
            self.transform_signal_icosine,
            self.transform_signal_wht,
            self.transform_signal_wht_inverse,
        ]
        operated_signal = self._get_signal_from_combobox("sygnalComboBox")[1]
        self.operation_result = operation_types[operation_type](operated_signal)
        self._fill_stats_tab(
            SignalTypes.MIXED,
            self.operation_result,
            operated_signal if operation_type == 2 else None,
        )

    def multi_argument_operation(self):
        signal_1 = self._get_signal_from_combobox("sygnal1DwuComboBox")[1]
        signal_2 = self._get_signal_from_combobox("sygnal2DwuComboBox")[1]
        operation_type = self.ui.operacjaDwuComboBox.currentIndex()
        self.operation_result = self.multi_argument_operations[operation_type](
            signal_1, signal_2
        )
        self._fill_stats_tab(SignalTypes.MIXED, self.operation_result)
        self._plot_signal(SignalTypes.MIXED, self.operation_result, PlotTypes.LINE)
