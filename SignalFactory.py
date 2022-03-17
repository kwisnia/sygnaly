from typing import Callable
from Signal import Signal
from functions import SAMPLES


class SignalFactory:
    def create(
        self,
        amplitude: float,
        signal_start_time: float,
        signal_duration: float,
        frequency: int,
        type_of_signal: Callable,
        fullfilment: float or int = None,
        sample_rate: float = None,
    ):
        name = "".join([str(elem) for elem in type_of_signal.__name__.split("_")[1:]])
        if sample_rate is None:
            sample_rate = SAMPLES / signal_duration
        samples, values = type_of_signal(
            amplitude,
            signal_duration,
            frequency,
            signal_start_time,
            fullfilment,
            sample_rate,
        )
        return Signal(signal_start_time, signal_duration, samples, values, name, frequency, sample_rate)
