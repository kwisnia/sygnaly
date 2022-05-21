from signal import signal
from time import sleep
from distance.Environment import Environment
from PySide6 import QtWidgets, QtCore
from distance.DistanceSensor import DistanceSensor
from gui.custom_widgets.PlotTypes import PlotTypes
from gui.custom_widgets.PlotWidget import PlotWidget

from gui.ui_distancewindow import Ui_DystansWidget


class Worker(QtCore.QThread):
    progress = QtCore.Signal(tuple)
    finished = QtCore.Signal()

    def run(self):
        print(time_unit)
        sensor = DistanceSensor(
            signal_period[0],
            sampling_rate[0],
            buffer_length[0],
            reporting_period[0],
        )
        env = Environment(
            time_unit[0],
            signal_speed[0],
            item_speed[0],
            sensor,
            item_distance[0],
        )
        while not self.isInterruptionRequested():
            env.step()
            sleep(time_unit[0])
            self.progress.emit((sensor, env))
        self.finished.emit()


class SimulatorWindow(QtWidgets.QWidget):
    def __init__(self):
        super(SimulatorWindow, self).__init__()
        self.ui = Ui_DystansWidget()
        self.ui.setupUi(self)
        self.probingSignalWidget = PlotWidget(800, 240, None, False)
        self.feedbackSignalWidget = PlotWidget(800, 240, None, False)
        self.correlationSignalWidget = PlotWidget(800, 240, None, False)
        self.ui.wykresy1Layout.addChildWidget(self.probingSignalWidget)
        self.ui.wykresy2Layout.addChildWidget(self.feedbackSignalWidget)
        self.ui.wykresy3Layout.addChildWidget(self.correlationSignalWidget)
        self.ui.startButton.clicked.connect(self.start_simulation)

    def start_simulation(self):
        global signal_period
        global sampling_rate
        global buffer_length
        global reporting_period
        global time_unit
        global signal_speed
        global item_speed
        global item_distance
        signal_period = (self.ui.okresSygnaluDoubleSpinBox.value(),)
        sampling_rate = (self.ui.czestotliwoscProbkowaniaDoubleSpinBox.value(),)
        buffer_length = (self.ui.dlugoscBuforuDoubleSpinBox.value(),)
        reporting_period = (self.ui.okresRaportowaniaDoubleSpinBox.value(),)
        time_unit = (self.ui.jednostkaCzasuDoubleSpinBox.value(),)
        signal_speed = (self.ui.predkoscSygnaluDoubleSpinBox.value(),)
        item_speed = (self.ui.rzeczywistaPredkoscDoubleSpinBox.value(),)
        item_distance = (self.ui.dystansOdCzujnikaDoubleSpinBox.value(),)
        # Step 2: Create a QThread object
        self.thread = Worker()
        # Step 4: Move worker to the thread
        self.thread.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

    def reportProgress(self, objects):
        # print(objects)
        self.probingSignalWidget.update(
            objects[0].probe_signal.samples, objects[0].probe_signal.values
        )
        self.feedbackSignalWidget.update(
            objects[0].feedback_signal.samples,
            objects[0].feedback_signal.values,
        )
        self.correlationSignalWidget.update(
            objects[0].correlated_signal.samples,
            objects[0].correlated_signal.values,
        )
        self.ui.statystykiWidget.item(0, 0).setText(str(objects[1].timestamp))
        self.ui.statystykiWidget.item(1, 0).setText(str(objects[1].item_distance))
        self.ui.statystykiWidget.item(2, 0).setText(str(objects[0].distance))
