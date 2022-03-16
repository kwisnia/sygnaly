from typing import Callable

class Signal:
    def __init__(
        self,
        amplitude: float,
        signal_start_time: float,
        signal_duration: float,
        frequency: int,
        type_of_signal: Callable,
        fullfilment: float = None,
    ):
        self.signal_start_time = signal_start_time
        self.signal_duration = signal_duration
        self.frequency = frequency
        self.samples, self.values = type_of_signal(
            amplitude, signal_duration, frequency, signal_start_time, fullfilment
        )
        self.name = "".join(
            [str(elem) for elem in type_of_signal.__name__.split("_")[1:]])
        self.fullfilment = fullfilment
