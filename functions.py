from random import random
import numpy as np
import json
from Signal import Signal

SAMPLES = 1000


def save_to_file(signal: Signal, file_name: str):
    name = file_name + ".json"
    output = open(name, "w")
    signal_dict = {
        "signal_start_time": signal.signal_start_time,
        "signal_duration": signal.signal_duration,
        "samples": signal.samples,
        "values": signal.values,
        "name": signal.name,
        "frequency": signal.frequency,
        "sample_rate": signal.sample_rate,
    }
    json.dump(signal_dict, output, indent=6)
    output.close()


def load_from_file(filename: str):
    input_file = open(filename)
    signal_dict = json.load(input_file)
    input_file.close()
    return Signal(
        signal_dict["signal_start_time"],
        signal_dict["signal_duration"],
        signal_dict["samples"],
        signal_dict["values"],
        signal_dict["name"],
        signal_dict["frequency"],
        signal_dict["sample_rate"],
    )


def generate_gauss_noise(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = 0,
):
    generator = np.random.default_rng()
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list([generator.normal(0, 1.0) for _ in samples])
    return samples, values


def generate_uniform_noise(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = 0,
):
    generator = np.random.default_rng()
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list([generator.uniform(-amplitude, amplitude) for _ in samples])
    return samples, values


def generate_sinusoidal_signal(
    amplitude: float,
    length: float,
    frequency: int,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = 0,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        amplitude * np.sin(2 * np.pi * frequency * (sample - start))
        for sample in samples
    )
    return samples, values


def generate_sinusoidal_signal_one_half_straight(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = 0,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        amplitude * np.sin(2 * np.pi * frequency * (sample - start))
        if amplitude * np.sin(2 * np.pi * frequency * (sample - start)) > 0
        else 0
        for sample in samples
    )
    return samples, values


def generate_sinusoidal_signal_straight(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = None,
    sample_rate: float = None,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        (
            abs(amplitude * np.sin(2 * np.pi * frequency * (sample - start)))
            for sample in samples
        )
    )
    return samples, values


def generate_rectangle_signal(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = None,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        amplitude
        if ((sample - start) * frequency) - np.floor((sample - start) * frequency)
        < fulfillment
        else 0
        for sample in samples
    )
    return samples, values


def generate_rectangle_signal_symmetric(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = None,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        amplitude
        if ((sample - start) * frequency) - np.floor((sample - start) * frequency)
        < fulfillment
        else -amplitude
        for sample in samples
    )
    return samples, values


def generate_triangle_signal(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = None,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        (amplitude / (fulfillment * frequency)) * (sample - (frequency * int(sample / frequency)) - start)
        if 
            (frequency * int(sample / frequency)) + start <= sample < (fulfillment * frequency) + (frequency * int(sample / frequency)) + start
        else 
            -(amplitude / (frequency * (1 - fulfillment))) * (sample - (frequency * int(sample / frequency)) - start) + (amplitude / (1 - fulfillment))
        for sample in samples 
    )
    return samples, values


def generate_unit_jump_signal(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
    sample_rate: float = None,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        amplitude
        if sample > fulfillment
        else 0.5 * amplitude
        if sample == fulfillment
        else 0
        for sample in samples
    )
    return samples, values


def generate_unit_impulse(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    breakpoint_index: int = 0,
    sample_rate: float = 0,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(
        0 if i != breakpoint_index - 1 else amplitude for i in range(len(samples))
    )
    return samples, values


def generate_impulse_noise(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    amplitude_probability: float = 0,
    sample_rate: float = 0,
):
    samples = list(np.linspace(start, start + length, int(sample_rate * length)))
    values = list(amplitude if random() < amplitude_probability else 0 for _ in samples)
    return samples, values


# ▪ (S1) szum o rozkładzie jednostajnym
# ▪ (S2) szum gaussowski
# ▪ (S3) sygnał sinusoidalny
# ▪ (S4) sygnał sinusoidalny wyprostowany jednopołówkowo
# ▪ (S5) sygnał sinusoidalny wyprostowany dwupołówkowo
# ▪ (S6) sygnał prostokątny
# ▪ (S7) sygnał prostokątny symetryczny
# ▪ (S8) sygnał trójkątny
# ▪ (S9) skok jednostkowy
# ▪ (S10) impuls jednostkowy
# ▪ (S11) szum impulsowy
