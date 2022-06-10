from copy import deepcopy
from math import ceil
import numpy as np
from scipy.linalg import hadamard
from scipy import fft
from Signal import Signal


def c(m, N):
    if m == 0:
        return np.sqrt(1 / N)
    else:
        return np.sqrt(2 / N)


def fast_cosine_transform(signal: Signal):
    """
    Fast cosine transform.
    """
    new_signal = deepcopy(signal)
    N = len(new_signal.values)
    new_signal.values = np.empty_like(signal.values)
    for i in range(N // 2):
        new_signal.values[i] = signal.values[i * 2]
        new_signal.values[N - i - 1] = signal.values[i * 2 + 1]
    dft_new_values = dit_fft(new_signal)
    for i in range(N):
        new_signal.values[i] = (
            c(i, N) * np.exp(-1j * np.pi * i / (2 * N)) * dft_new_values.values[i]
        ).real
    return new_signal


def inverse_fast_cosine_transform(signal: Signal):
    new_signal = deepcopy(signal)
    # new_signal.values = fft.idct(signal.values)
    # return new_signal
    new_values = []
    for i in range(len(new_signal.values)):
        new_values.append(
            c(i, len(new_signal.values))
            * np.exp(1j * np.pi * i / (2 * len(new_signal.values)))
            * new_signal.values[i]
        )
    new_signal.values = new_values
    inversed = inverse_dit_fft(new_signal)
    new_signal.values = np.empty_like(inversed.values)
    for i in range(len(new_signal.values) // 2):
        new_signal.values[2 * i] = inversed.values[i]
        new_signal.values[2 * i + 1] = inversed.values[len(new_signal.values) - 1 - i]
    new_signal.values *= len(new_signal.values)
    return new_signal


def walsh_hadamard_transform(signal: Signal, inverted=False):
    """
    Walsh Hadamard transform.
    """
    # pad signal values with zeros until it is a power of 2 long
    signal_length = len(signal.values)
    if signal_length & (signal_length - 1) != 0:
        signal_length = 2 ** ceil(np.log2(signal_length))
        signal.values = np.pad(
            signal.values,
            (0, signal_length - len(signal.values)),
            "constant",
            constant_values=(0, 0),
        )
        signal.samples = np.pad(
            signal.samples,
            (0, signal_length - len(signal.samples)),
            "constant",
            constant_values=(0, 0),
        )
    # apply hadamard transform
    new_signal = deepcopy(signal)
    new_signal.values = hadamard(signal_length) @ signal.values
    if inverted:
        new_signal.values *= 1 / signal_length
    return new_signal
    # hadamard_matrix = hadamard(m)
    # new_signal = deepcopy(signal)
    # new_signal.values = np.matmul(hadamard_matrix, signal.values)
    # return new_signal


def dft(signal: Signal):
    new_signal = deepcopy(signal)
    f0 = signal.sample_rate / len(signal.values)
    new_signal.samples = np.arange(len(signal.values)) * f0
    new_signal_values = []
    for i in range(len(new_signal.values)):
        inner_sum = 0
        for k in range(len(new_signal.values)):
            inner_sum += new_signal.values[k] * np.exp(
                -1j * (2 * np.pi * i / len(new_signal.values)) * k
            )
        new_signal_values.append(1 / len(new_signal.values) * inner_sum)
    new_signal.values = new_signal_values
    return new_signal


def inverse_dft(signal: Signal):
    new_signal = deepcopy(signal)
    new_signal.samples = np.linspace(
        signal.signal_start_time,
        signal.signal_start_time + signal.signal_duration,
        int(signal.sample_rate * signal.signal_duration),
    )
    new_signal_values = []
    for i in range(len(new_signal.values)):
        inner_sum = 0
        for k in range(len(new_signal.values)):
            inner_sum += new_signal.values[k] * np.exp(
                1j * (2 * np.pi * i / len(new_signal.values)) * k
            )
        new_signal_values.append(inner_sum)
    new_signal.values = new_signal_values
    return new_signal


def dit_fft(signal: Signal):
    new_signal = deepcopy(signal)
    f0 = signal.sample_rate / len(signal.values)
    new_signal.samples = np.arange(len(signal.values)) * f0
    new_signal.values = 1 / len(signal.values) * fft(signal.values)
    return new_signal


def fft(values: list[float], inverted=False):
    N = len(values)
    multiplicator = 2 if inverted else -2
    if N == 2:
        return np.array(
            [values[0] + values[1], values[0] - values[1]], dtype=np.complex
        )
    even_samples = fft(values[::2], inverted)
    odd_samples = fft(values[1::2], inverted)
    w = np.exp(multiplicator * np.pi * 1j * np.arange(N // 2) / N)
    X = np.hstack((even_samples + w * odd_samples, even_samples - w * odd_samples))
    return X


def inverse_dit_fft(signal: Signal):
    new_signal = deepcopy(signal)
    new_signal.samples = np.linspace(
        signal.signal_start_time,
        signal.signal_start_time + signal.signal_duration,
        int(signal.sample_rate * signal.signal_duration),
    )
    new_signal.values = fft(signal.values, inverted=True)
    return new_signal
