from random import sample
import numpy as np


def generate(type):
    pass


def generate_gauss_noise(
    frequency: int, amplitude: float, length: float, start: float = 0
):
    generator = np.random.default_rng()
    samples = list(np.arange(start, start + length, 1 / frequency))
    values = list([generator.normal(0, 1.0) for _ in samples])
    return samples, values


def generate_uniform_noise(
    frequency: int, amplitude: float, length: float, start: float = 0
):
    generator = np.random.default_rng()
    samples = list(np.arange(start, start + length, 1 / frequency))
    values = list([generator.uniform(-amplitude, amplitude) for _ in samples])
    return samples, values


def generate_sinusoidal_signal(
    frequency: int, amplitude: float, length: float, start: float = 0
):
    samples = list(np.arange(start, start + length, 1 / frequency))
    values = list(
        amplitude * np.sin(2 * np.pi / frequency * (sample - start))
        for sample in samples
    )
    return samples, values


def generate_sinusoidal_signal_one_half_straight(
    frequency: int, amplitude: float, length: float, start: float = 0
):
    samples = list(np.arange(start, start + length, 1 / frequency))
    values = list(
        amplitude * np.sin(sample) if np.sin(sample) > 0 else 0 for sample in samples
    )
    return samples, values


def generate_sinusoidal_signal_straight(
    frequency: int, amplitude: float, length: float, start: float = 0
):
    samples = list(np.arange(start, start + length, 1 / frequency))
    values = list((abs(amplitude * np.sin(sample)) for sample in samples))
    return samples, values


def generate_rectangle_signal():
    pass


def generate_rectangle_signal_symmetric():
    pass


def generate_triangle_signal():
    pass


def generate_unit_jump_signal():
    pass


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
