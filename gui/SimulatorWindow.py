from distance.Environment import Environment
from PySide6 import QtWidgets, QtCore
from distance.DistanceSensor import DistanceSensor
from gui.custom_widgets.PlotTypes import PlotTypes
from gui.custom_widgets.PlotWidget import PlotWidget

from gui.ui_distancewindow import Ui_DystansWidget


class Worker(QtCore.QObject):
    progress = QtCore.Signal(tuple)
    finished = QtCore.Signal()

    def run(self, ui):
        sensor = DistanceSensor(
            ui.okresRaportowaniaDoubleSpinBox.value(),
            ui.czestotliwoscProbkowaniaDoubleSpinBox.value(),
            ui.dlugoscBuforuDoubleSpinBox.value(),
            ui.okresRaportowaniaDoubleSpinBox.value(),
        )
        env = Environment(
            ui.jednostkaCzasuDoubleSpinBox.value(),
            ui.predkoscSygnaluDoubleSpinBox.value(),
            ui.rzeczywistaPredkoscDoubleSpinBox.value(),
            sensor,
            ui.dystansOdCzujnikaDoubleSpinBox.value(),
        )
        while True:
            env.step()
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

        # Step 2: Create a QThread object
        self.thread = QtCore.QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(lambda: self.worker.run(self.ui))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

    def reportProgress(self, objects):
        self.probingSignalWidget.plot(
            objects[0].probe_signal.samples, objects[0].probe_signal.values, PlotTypes.LINE
        )
        self.feedbackSignalWidget.plot(
            objects[0].feedback_signal.samples,
            objects[0].feedback_signal.values,
            PlotTypes.LINE,
        )
        self.correlationSignalWidget.plot(
            objects[0].correlated_signal.samples,
            objects[0].correlated_signal.values,
            PlotTypes.LINE,
        )
        self.ui.statystykiWidget.item(0, 0).setText(str(objects[1].timestamp))
        self.ui.statystykiWidget.item(1, 0).setText(str(objects[1].item_distance))
        self.ui.statystykiWidget.item(2, 0).setText(str(objects[0].distance))
