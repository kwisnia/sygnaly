import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from SignalFactory import SignalFactory
from filters import high_pass_filter, low_pass_filter
from functions import *
from gui.custom_widgets.PlotTypes import PlotTypes
from gui.custom_widgets.PlotWidget import PlotWidget
from gui.ui_mainwindow import Ui_MainWindow


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
        self.leftGraphWidget = PlotWidget()
        self.leftHistWidget = PlotWidget()
        self.rightGraphWidget = PlotWidget()
        self.rightHistWidget = PlotWidget()
        self.resultGraphWidget = PlotWidget(560, 380)
        self.resultHistWidget = PlotWidget(560, 380)
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
            if selected_signal_type == 12 or selected_signal_type == 13
            else self._get_combobox_value(f"typOknaComboBox_{selected_signal_type}"),
        )
        plot_type = PlotTypes.LINE
        if selected_signal_type == 10 or selected_signal_type == 11:
            plot_type = PlotTypes.SCATTER
        elif selected_signal_type == 12 or selected_signal_type == 13:
            plot_type = PlotTypes.STEM
        if second_signal:
            self.right_signal = generated_signal
            self.rightGraphWidget.plot(
                generated_signal.samples, generated_signal.values, plot_type
            )
            self.rightHistWidget.plot(
                generated_signal.samples, generated_signal.values, PlotTypes.HISTOGRAM
            )
        else:
            self.left_signal = generated_signal
            self.leftGraphWidget.plot(
                generated_signal.samples, generated_signal.values, plot_type
            )
            self.leftHistWidget.plot(
                generated_signal.samples, generated_signal.values, PlotTypes.HISTOGRAM
            )
