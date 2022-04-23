from Signal import Signal
import numpy as np
from functions import SAMPLES
import math


def avg_signal_value(signal: Signal):
    value = (
        (1 / (signal.samples[-1] - signal.samples[0]))
        * np.sum(signal.values)
        * signal.signal_duration
        / SAMPLES
    )
    return value


def abs_avg_signal_value(signal: Signal):
    value = (
        (1 / (signal.samples[-1] - signal.samples[0]))
        * np.sum(np.absolute(signal.values))
        * signal.signal_duration
        / SAMPLES
    )
    return value


def avg_signal_power(signal: Signal):
    value = (
        (1 / (signal.samples[-1] - signal.samples[0]))
        * np.sum(np.power(signal.values, 2))
        * signal.signal_duration
        / SAMPLES
    )
    return value


def variance_signal_value(signal: Signal):
    avg_signal_val = avg_signal_value(signal)
    value = (
        (1 / (signal.samples[-1] - signal.samples[0]))
        * np.sum(np.power(np.subtract(signal.values, avg_signal_val), 2))
        * signal.signal_duration
        / SAMPLES
    )
    return value


def rms_signal_value(signal: Signal):
    value = np.sqrt(avg_signal_power(signal))
    return value


def mean_square_error(original_signal, reconstructed_signal):
    return sum(
        [
            (original_signal.values[i] - reconstructed_signal.values[i]) ** 2
            for i in range(len(original_signal.samples))
        ]
    ) / len(original_signal.values)


def signal_to_noise_ratio(original_signal, reconstructed_signal):
    return 10 * math.log(
        (
            sum((np.array(original_signal.values) ** 2))
            / sum(
                [
                    (original_signal.values[i] - reconstructed_signal.values[i]) ** 2
                    for i in range(len(original_signal.samples))
                ]
            )
        ),
        10,
    )


def peak_signal_to_noise_ratio(original_signal, reconstructed_signal):
    return 10 * math.log(
        max(original_signal.values)
        / mean_square_error(original_signal, reconstructed_signal),
        10,
    )


def maximum_difference(original_signal, reconstructed_signal):
    return max(
        [
            original_signal.values[i] - reconstructed_signal.values[i]
            for i in range(len(original_signal.samples))
        ]
    )
