import functions as fn
from Signal import Signal
from plot import plot

if __name__ == "__main__":
    signal = Signal(
        amplitude=5,
        signal_start_time=0,
        signal_duration=5,
        frequency=100,
        type_of_signal=fn.generate_sinusoidal_signal,
    )
    signal.save_to_file()
    plot(signal)
