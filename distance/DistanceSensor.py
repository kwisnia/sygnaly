import operator
from SignalFactory import SignalFactory
from functions import generate_rectangle_signal, generate_sinusoidal_signal, generate_triangle_signal
from operations import add, corelate
import numpy as np


class DistanceSensor:
    def __init__(
        self, probe_signal_period, sample_rate, buffer_len, report_period
    ) -> None:
        self.probe_signal_period = probe_signal_period
        self.sample_rate = sample_rate
        self.buffer_len = buffer_len
        self.report_period = report_period
        self.calculation_timestamp = float("-inf")
        self.distance = 0
        self.signal_factory = SignalFactory()

    def generate_probing_signal(self, range_start, delay=0.0):
        sig_len = (1 / self.sample_rate) * self.buffer_len
        first_signal = self.signal_factory.create(
            1,
            range_start + delay,
            sig_len,
            self.probe_signal_period,
            self.sample_rate,
            generate_sinusoidal_signal,
        )
        second_signal = self.signal_factory.create(
            0.6,
            range_start + delay,
            sig_len,
            self.probe_signal_period / 6 * 2,
            self.sample_rate,
            generate_rectangle_signal,
            0.3,
        )
        return add(first_signal, second_signal)

    def update(self, delay, timestamp, signal_velocity):
        start_time = timestamp - self.buffer_len / self.sample_rate

        # wyznacz wartosci sygnalu probujacego
        self.probe_signal = self.generate_probing_signal(start_time)
        # wyznacz wartosci sygnalu zwrotnego
        self.feedback_signal = self.generate_probing_signal(start_time, delay)

        if (timestamp - self.calculation_timestamp) >= self.report_period:
            self.calculation_timestamp = timestamp
            self.calculate_distance(signal_velocity)

    def calculate_distance(self, signal_velocity):
        # skoreluj sygnal zwrotny z przeszukujacym
        self.correlated_signal = corelate(self.feedback_signal, self.probe_signal)

        index = np.argmax(
            self.correlated_signal.values[: len(self.correlated_signal.values) // 2]
        )

        delay = index / self.sample_rate
        self.distance = delay * signal_velocity / 2.0
