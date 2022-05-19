from copy import deepcopy
from Signal import Signal
import numpy as np
import matplotlib.pyplot as plt


def quantize_rounded(sampled_signal: Signal, bit_numer: int):
    qunatization_levels = np.linspace(
        np.min(sampled_signal.values),
        np.max(sampled_signal.values),
        2**bit_numer,
    )
    quantized_values = []
    for value in sampled_signal.values:
        quantized_values.append(
            qunatization_levels[(np.abs(qunatization_levels - value)).argmin()]
        )
    quantized_signal = deepcopy(sampled_signal)
    quantized_signal.values = np.array(quantized_values)
    return quantized_signal
