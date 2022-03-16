class Signal:
    def __init__(
        self,
        signal_start_time: float,
        signal_duration: float,
        samples: list[float],
        values: list[float],
        name: str,
        sample_rate: float,
    ):
        self.signal_start_time = signal_start_time
        self.signal_duration = signal_duration
        self.samples, self.values = samples, values
        self.name = name
        self.sample_rate = sample_rate
