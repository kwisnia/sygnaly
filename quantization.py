from copy import copy
from Signal import Signal
import numpy as np
import matplotlib.pyplot as plt


def quantize_rounded(
    sampled_signal: Signal, bit_numer: int, original_signal: Signal = None
):
    qunatization_levels = np.linspace(
        np.min(original_signal.values),
        np.max(original_signal.values),
        2 ** bit_numer,
    )
    quantized_values = []
    for value in sampled_signal.values:
        quantized_values.append(
            qunatization_levels[(np.abs(qunatization_levels - value)).argmin()]
        )
    quantized_signal = copy(sampled_signal)
    quantized_signal.values = np.array(quantized_values)
    plt.scatter(sampled_signal.samples, quantized_values)
    plt.plot(original_signal.samples, original_signal.values)
    plt.title("Kwantyzacja równomierna z zaokrągleniem")
    plt.legend(["Wynik kwantyzacji", "Oryginalny sygnał"])
    plt.show()
    return quantized_signal
