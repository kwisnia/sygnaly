import numpy as np

from windows import blackman_window, rectangular_window


def low_pass_filter(filter_order, cutoff_frequency, sample_rate, window_type):
    if window_type == 1:
        window = [
            blackman_window(filter_order, sample_index)
            for sample_index in range(filter_order)
        ]
    else:
        window = [rectangular_window() for _ in range(filter_order)]
    k = sample_rate / cutoff_frequency
    center_sample = (filter_order - 1) / 2
    return np.array(
        [
            2 / k
            if sample_index == center_sample
            else np.sin(2 * np.pi * (sample_index - center_sample) / k)
            / (np.pi * (sample_index - center_sample))
            for sample_index in range(filter_order)
        ]
    ) * np.array(window)


def high_pass_filter(filter_order, cutoff_frequency, sample_rate, window_type):
    return np.array(
        [
            x * (-1) ** i
            for i, x in enumerate(
                low_pass_filter(
                    filter_order, cutoff_frequency, sample_rate, window_type
                )
            )
        ]
    )
