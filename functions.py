import numpy as np
import json
from Signal import Signal 
from SignalFile import SignalFile
SAMPLES = 1000


def save_to_file(signal: Signal):
    name = signal.name + ".json"
    output = open(name, "w")
    signal_dict = {
        "signal_start_time": signal.signal_start_time,
        "signal_duration": signal.signal_duration,
        "frequency": signal.frequency,
        "samples": signal.samples,
        "values": signal.values,
        "name": signal.name,
        "fullfilment": signal.fullfilment,
    }
    json.dump(signal_dict, output, indent=6)
    output.close()

def load_from_file(filename: str):
    input_file = open(filename)
    signal_dict = json.load(input_file)
    input_file.close()
    return SignalFile(signal_dict)


def generate_gauss_noise(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
):
    generator = np.random.default_rng()
    samples = list(np.linspace(start, start + length, SAMPLES))
    values = list([generator.normal(0, 1.0) for _ in samples])
    return samples, values


def generate_uniform_noise(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
):
    generator = np.random.default_rng()
    samples = list(np.linspace(start, start + length, SAMPLES))
    values = list([generator.uniform(-amplitude, amplitude) for _ in samples])
    return samples, values


def generate_sinusoidal_signal(
    amplitude: float,
    length: float,
    frequency: int,
    start: float = 0,
    fulfillment: float = 0,
):
    samples = list(np.linspace(start, start + length, SAMPLES))
    print(samples)
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
):
    samples = list(np.linspace(start, start + length, SAMPLES))
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
    fulfillment: float = 0,
):
    samples = list(np.linspace(start, start + length, SAMPLES))
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
):
    samples = list(np.linspace(start, start + length, SAMPLES))
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
):
    samples = list(np.linspace(start, start + length, SAMPLES))
    values = list(
        amplitude
        if ((sample - start) * frequency) - np.floor((sample - start) * frequency)
        < fulfillment
        else -amplitude
        for sample in samples
    )
    return samples, values


def generate_triangle_signal(amplitude: float, length: float, frequency: int = 0, start: float = 0
                             ):
    samples = list(np.arange(start, start + length, 1 / FREQUENCY))
    values = list(2 * np.abs(((sample * 2 * frequency - 0.5) % 2) - 1) - 1 for sample in samples)
    return samples, values


def generate_unit_jump_signal(
    amplitude: float,
    length: float,
    frequency: int = 0,
    start: float = 0,
    fulfillment: float = 0,
):
    samples = list(np.linspace(start, start + length, SAMPLES))
    values = list(
        amplitude
        if sample > fulfillment
        else 0.5 * amplitude
        if sample == fulfillment
        else 0
        for sample in samples
    )
    return samples, values


def generate_unit_impulse():
    pass


def generate_impulse_noise():
    pass


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
