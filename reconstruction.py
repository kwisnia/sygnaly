import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from Signal import Signal
from copy import copy


def zero_order_hold(reconstructed_signal: Signal, original_signal: Signal = None):
    # plt.step(
    #     reconstructed_signal.samples,
    #     reconstructed_signal.values,
    # )
    zero_order_hold_values = [
        reconstructed_signal.values[
            np.searchsorted(reconstructed_signal.samples, x) - 1
        ]
        for x in original_signal.samples
    ]
    plt.plot(original_signal.samples, zero_order_hold_values)
    plt.plot(original_signal.samples, original_signal.values)
    new_signal = copy(original_signal)
    new_signal.values = np.array(zero_order_hold_values)
    plt.title("Rekonstrukcja sygnału Zero Order Hold")
    plt.legend(["Rekonstrukcja sygnału", "Oryginalny sygnał"])
    plt.show()
    return new_signal


def first_order_hold(reconstructed_signal: Signal, original_signal: Signal = None):
    first_order_hold_values = []
    prev_desired_index = -1
    for x in original_signal.samples:
        desired_index = np.searchsorted(reconstructed_signal.samples, x)
        if desired_index != prev_desired_index:
            prev_desired_index = desired_index
            params = linregress(
                [
                    reconstructed_signal.samples[desired_index - 1],
                    reconstructed_signal.samples[desired_index],
                ],
                [
                    reconstructed_signal.values[desired_index - 1],
                    reconstructed_signal.values[desired_index],
                ],
            )
        first_order_hold_values.append(params.slope * x + params.intercept)
    new_signal = copy(original_signal)
    new_signal.values = np.array(first_order_hold_values)
    plt.plot(
        original_signal.samples,
        first_order_hold_values,
    )

    plt.plot(original_signal.samples, original_signal.values)
    plt.title("Rekonstrukcja sygnału First Order Hold")
    plt.legend(["Rekonstrukcja sygnału", "Oryginalny sygnał"])
    plt.show()
    return new_signal


def sinc(reconstructed_signal: Signal, original_signal: Signal = None):
    new_samples = []
    for i in range(len(original_signal.samples)):
        sample_value = 0
        for j in range(len(reconstructed_signal.samples)):
            sample_value += reconstructed_signal.values[j] * np.sinc(
                original_signal.samples[i] * reconstructed_signal.sample_rate - j
            )
        new_samples.append(sample_value)
    new_signal = copy(original_signal)
    new_signal.values = np.array(new_samples)
    # plt.scatter(reconstructed_signal.samples, reconstructed_signal.values)
    plt.plot(original_signal.samples, new_samples)
    plt.plot(original_signal.samples, original_signal.values)
    plt.title("Rekonstrukcja sygnału funkcją sinc")
    plt.legend(["Rekonstrukcja sygnału", "Oryginalny sygnał"])
    plt.show()
    return new_signal
