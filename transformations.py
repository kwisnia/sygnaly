from copy import deepcopy
import numpy as np
from scipy.linalg import hadamard
from scipy import fft
from Signal import Signal

def fast_cosine_transform(signal: Signal):
    """
    Fast cosine transform.
    """
    new_signal = deepcopy(signal)
    new_signal.values = fft.dct(signal.values)
    return new_signal

def walsh_hadamard_transform(signal: Signal):
    """
    Walsh Hadamard transform.
    """
    m = round(np.log(len(signal.values)) / np.log(2))
    hadamard_matrix = hadamard(m)
    new_signal = deepcopy()
    new_signal.values = np.matmul(hadamard_matrix, signal.values)
    return new_signal


def frequency_fft(signal: Signal):
    new_signal = deepcopy()
    new_signal.samples = np.fft.fftfreq(len(signal.samples))
    new_signal.values = np.fft.fft(signal.values)
    return new_signal
    