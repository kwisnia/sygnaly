from Signal import Signal
import numpy as np
from functions import SAMPLES


def avg_signal_value(signal: Signal):
    # if (signal.frequency is not None):
    #    num_of_samples_in_interval = (len(signal.samples) / signal.signal_duration) / signal.frequency
    #    print(num_of_samples_in_interval)
    #    unnecessary_samples = len(signal.samples) % num_of_samples_in_interval
    #    print(unnecessary_samples)
    #    valid_samples = signal.samples[:len(signal.samples) - int(unnecessary_samples)]
    #    value = (
    #        1 / (valid_samples[-1] - valid_samples[0] + 1)) * np.sum(signal.values[:len(signal.samples) - unnecessary_samples])
    # else:
    value = (1 / (signal.samples[-1] - signal.samples[0])) * np.sum(signal.values) * signal.signal_duration / SAMPLES 
    return value


def abs_avg_signal_value(signal: Signal):
    # if (signal.frequency is not None):
    #    pass
    # else:
    value = (1 / (signal.samples[-1] - signal.samples[0])) * np.sum(
        np.absolute(signal.values)  
    ) * signal.signal_duration / SAMPLES
    return value


def avg_signal_power(signal: Signal):
    # if (signal.frequency is not None):
    #    pass
    # else:
    value = (1 / (signal.samples[-1] - signal.samples[0])) * np.sum(
        np.power(signal.values, 2)
    ) * signal.signal_duration / SAMPLES
    return value


def variance_signal_value(signal: Signal):
    # if (signal.frequency is not None):
    #    pass
    # else:
    avg_signal_val = avg_signal_value(signal)
    value = (1 / (signal.samples[-1] - signal.samples[0])) * np.sum(
        np.power(np.subtract(signal.values, avg_signal_val), 2)
    ) * signal.signal_duration / SAMPLES
    return value


def rms_signal_value(signal: Signal):
    # if (signal.frequency is not None):
    #    pass
    # else:
    value = np.sqrt(avg_signal_power(signal))
    return value
