from Signal import Signal
import numpy as np
from copy import deepcopy


def add(first: Signal, second: Signal):
    if len(first.samples) == len(second.samples):
        new_signal = deepcopy(first)
        new_signal.values = list(np.add(first.values, second.values))
        return new_signal
    return False


def subtract(first: Signal, second: Signal):
    if len(first.samples) == len(second.samples):
        new_signal = deepcopy(first)
        new_signal.values = list(np.subtract(first.values, second.values))
        return new_signal
    return False


def multiply(first: Signal, second: Signal):
    if len(first.samples) == len(second.samples):
        new_signal = deepcopy(first)
        new_signal.values = list(np.multiply(first.values, second.values))
        return new_signal
    return False


def divide(first: Signal, second: Signal):
    if len(first.samples) == len(second.samples):
        new_signal = deepcopy(first)
        # new_signal.values = np.divide(first.values, second.values, out=np.zeros_like(first.values), where=second.values!=0)
        new_signal.values = list(
            f_sample / s_sample if s_sample != 0 else f_sample
            for f_sample, s_sample in zip(first.values, second.values)
        )
        return new_signal
    return False


# def convolve(first: Signal, second: Signal):
#     if len(second.samples) > len(first.samples):
#         first, second = second, first

#     new_signal = deepcopy(first)
#     new_signal.values = np.convolve(first.values, second.values)
#     new_samples = len(new_signal.values) - len(first.values) + 1
#     new_signal.samples.extend(
#         np.linspace(
#             first.samples[-1],
#             first.samples[-1] + (1 / first.sample_rate) * new_samples,
#             new_samples,
#         )[1:]
#     )
#     return new_signal


def convolve(first: Signal, second: Signal):
    if len(second.samples) > len(first.samples):
        first, second = second, first

    new_signal = deepcopy(first)
    new_values = len(first.values) + len(second.values) - 1
    new_signal.values = np.zeros(new_values)
    for i in range(len(first.values)):
        for j in range(len(second.values)):
            new_signal.values[i + j] += first.values[i] * second.values[j]
    new_samples = len(new_signal.values) - len(first.values) + 1
    new_signal.samples.extend(
        np.linspace(
            first.samples[-1],
            first.samples[-1] + (1 / first.sample_rate) * new_samples,
            new_samples,
        )[1:]
    )
    return new_signal


def corelate(first: Signal, second: Signal):
    if len(second.samples) > len(first.samples):
        first, second = second, first
    new_signal = deepcopy(first)
    new_signal.values = np.convolve(first.values, second.values[::-1])
    new_samples = len(new_signal.values) - len(first.values)
    new_signal.samples.extend(
        np.linspace(
            first.samples[-1],
            first.samples[-1] + (1 / first.sample_rate) * new_samples,
            new_samples,
        )[1:]
    )
    return new_signal
