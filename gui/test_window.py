import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from filters import high_pass_filter, low_pass_filter
from functions import *
from gui.custom_widgets.PlotWidget import PlotWidget
from gui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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
        self.selected_signal_type = generate_gauss_noise
        # self.ui.wykresLewyLayout.addWidget(PlotWidget())
