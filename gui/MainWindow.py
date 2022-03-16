from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

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

        self.signal = QtWidgets.QComboBox()
        self.signal.addItems(self.signals)

        self.signal.currentIndexChanged.connect(self.show_fields)
        self.signal_start = QtWidgets.QDoubleSpinBox()
        self.signal_length = QtWidgets.QDoubleSpinBox()
        self.amplitude = QtWidgets.QDoubleSpinBox()
        self.frequency = QtWidgets.QDoubleSpinBox()
        self.fullfilment = QtWidgets.QDoubleSpinBox()
        self.sample_rate = QtWidgets.QDoubleSpinBox()
        self.signal_start_text = QtWidgets.QLabel("Początek sygnału")
        self.signal_length_text = QtWidgets.QLabel("Długość sygnału")
        self.amplitude_text = QtWidgets.QLabel("Amplituda")
        self.frequency_text = QtWidgets.QLabel("Częstotliwość")
        self.fullfilment_text = QtWidgets.QLabel("Długość okresu")
        self.sample_rate_text = QtWidgets.QLabel("Częstotliwość próbkowania")

        self.signal_start_text.setBuddy(self.signal_start)
        self.signal_length_text.setBuddy(self.signal_length)
        self.amplitude_text.setBuddy(self.amplitude)
        self.frequency_text.setBuddy(self.frequency)
        self.fullfilment_text.setBuddy(self.fullfilment)
        self.sample_rate_text.setBuddy(self.sample_rate)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(QtWidgets.QLabel("Typ sygnału"))
        self.layout.addWidget(self.signal)
        self.layout.addWidget(self.signal_start_text)
        self.layout.addWidget(self.signal_start)
        self.layout.addWidget(self.signal_length_text)
        self.layout.addWidget(self.signal_length)
        self.layout.addWidget(self.amplitude_text)
        self.layout.addWidget(self.amplitude)
        self.layout.addWidget(self.frequency_text)
        self.layout.addWidget(self.frequency)
        self.layout.addWidget(self.fullfilment_text)
        self.layout.addWidget(self.fullfilment)
        self.layout.addWidget(self.sample_rate_text)
        self.layout.addWidget(self.sample_rate)

    def show_fields(self, index):
        if index == 0:
            self.layout.removeWidget(self.amplitude_text)
            self.layout.removeWidget(self.amplitude)
            self.layout.removeWidget(self.frequency_text)
            self.layout.removeWidget(self.frequency)
            self.layout.removeWidget(self.fullfilment_text)
            self.layout.removeWidget(self.fullfilment)
            self.layout.removeWidget(self.sample_rate_text)
            self.layout.removeWidget(self.sample_rate)
