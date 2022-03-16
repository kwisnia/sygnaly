import argparse
import functions as fn
from SignalFactory import SignalFactory
from plot import plot_continuous, plot_discrete


if __name__ == "__main__":
    signal_factory = SignalFactory()
    signal = signal_factory.create(
        amplitude=1,
        signal_start_time=0,
        signal_duration=10,
        frequency=2,
        type_of_signal=fn.generate_unit_impulse,
        fullfilment=5,
        sample_rate=3,
    )
    plot_discrete(signal)
