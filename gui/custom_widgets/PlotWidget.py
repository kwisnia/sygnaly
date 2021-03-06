import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)
from gui.custom_widgets.PlotTypes import PlotTypes


class PlotWidget(QWidget):
    def __init__(self, width=580, height=300, parent=None, toolbar=True):
        super().__init__(parent)

        #  create widgets
        self.view = FigureCanvas(Figure(figsize=(3, 2)))
        self.axes = self.view.figure.subplots()
        (self.lines,) = self.axes.plot([], [])
        self.toolbar = NavigationToolbar2QT(self.view, self)
        #  Create layout
        vlayout = QVBoxLayout()
        if toolbar:
            vlayout.addWidget(self.toolbar)
        vlayout.addWidget(self.view)
        self.setLayout(vlayout)
        self.resize(width, height)

    def plot(self, x: list[float], y: list[float], plot_type: PlotTypes, clear=True):
        if clear:
            self.axes.clear()
        if plot_type == PlotTypes.LINE:
            self.axes.plot(x, y)
        elif plot_type == PlotTypes.HISTOGRAM:
            self.axes.hist(y)
        elif plot_type == PlotTypes.SCATTER:
            self.axes.scatter(x, y)
        elif plot_type == PlotTypes.STEM:
            self.axes.stem(x, y)
        elif plot_type == PlotTypes.STEP:
            self.axes.step(x, y)
        self.view.draw()

    def update(self, x: list[float], y: list[float]):
        self.lines.set_xdata(x)
        self.lines.set_ydata(y)
        self.axes.relim()
        self.axes.autoscale_view()
        self.view.draw()
        self.view.flush_events()
