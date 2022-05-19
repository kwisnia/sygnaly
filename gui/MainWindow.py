from copy import deepcopy
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from SignalFactory import SignalFactory
from filters import high_pass_filter, low_pass_filter
from functions import *
from gui.SignalTypes import SignalTypes
from gui.custom_widgets.PlotTypes import PlotTypes
from gui.custom_widgets.PlotWidget import PlotWidget
from gui.ui_mainwindow import Ui_MainWindow
from operations import add, convolve, corelate, divide, multiply, subtract
from quantization import quantize_rounded
from reconstruction import first_order_hold, sinc, zero_order_hold


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

        self.left_signal = None
        self.right_signal = None
        self.operation_result = None

        self.ui.wykresLewyLayout.addChildWidget(self.leftGraphWidget)
        self.ui.histogramLewyLayout.addChildWidget(self.leftHistWidget)
        self.ui.wykresPrawyLayout.addChildWidget(self.rightGraphWidget)
        self.ui.histogramPrawyLayout.addChildWidget(self.rightHistWidget)
        self.ui.wykresWynikowyLayout.addChildWidget(self.resultGraphWidget)
        self.ui.histogramWynikowyLayout.addChildWidget(self.resultHistWidget)
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

    def sample_signal(self):
        signal_to_sample = self._get_signal_from_combobox("sygnalComboBox")[1]
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
        # sampled_signal.values = np.array(sampled_signal.values)
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

    def quantize_signal(self):
        signal_to_quantize = self._get_signal_from_combobox("sygnalComboBox")[1]
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

    def reconstruct_signal(self):
        signal_to_reconstruct = self._get_signal_from_combobox("sygnalComboBox")[1]
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
            if selected_signal_type != 12 or selected_signal_type != 13
            else self._get_combobox_value(f"typOknaComboBox_{selected_signal_type}"),
        )
        plot_type = self._get_plot_type_from_index(selected_signal_type)
        if second_signal:
            self.right_signal = generated_signal
            self._plot_signal(SignalTypes.RIGHT, generated_signal, plot_type)
        else:
            self.left_signal = generated_signal
            self._plot_signal(SignalTypes.LEFT, generated_signal, plot_type)

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
        ]
        self.operation_result = operation_types[operation_type]()

    def multi_argument_operation(self):
        signal_1 = self._get_signal_from_combobox("sygnal1DwuComboBox")[1]
        signal_2 = self._get_signal_from_combobox("sygnal2DwuComboBox")[1]
        operation_type = self.ui.operacjaDwuComboBox.currentIndex()
        self.operation_result = self.multi_argument_operations[operation_type](
            signal_1, signal_2
        )
        self._plot_signal(SignalTypes.MIXED, self.operation_result, PlotTypes.LINE)
