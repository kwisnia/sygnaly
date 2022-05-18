import matplotlib.pyplot as plt
from Signal import Signal


def plot_continuous(signal: Signal):
    plt.figure(figsize=(7, 5))
    plt.axhline(linewidth=1, color="r", ls="-")
    plt.axvline(linewidth=1, color="r", ls="-")
    plt.plot(signal.samples, signal.values)
    plt.xlabel("t[s]")
    plt.ylabel("A")
    plt.show()


def plot_discrete(signal: Signal, second_signal: Signal = None):
    plt.figure(figsize=(7, 5))
    plt.axhline(linewidth=1, color="r", ls="-")
    plt.axvline(linewidth=1, color="r", ls="-")
    plt.stem(signal.samples, signal.values)
    plt.plot(second_signal.samples, second_signal.values)
    plt.xlabel("t[s]")
    plt.ylabel("A")
    plt.show()


def histogram(signal: Signal, bins: int):
    plt.figure(figsize=(5, 3))
    plt.hist(signal.values, bins=10)
    plt.show()
