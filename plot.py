import matplotlib.pyplot as plt
from Signal import Signal

def plot_continuous(signal: Signal):
   plt.plot(signal.samples, signal.values)
   plt.show()

def plot_discrete(signal: Signal):
   plt.scatter(signal.samples, signal.values)
   plt.show()

def histogram(signal: Signal, bins: int):
   plt.hist(signal.samples, signal.values, bins=bins)
   plt.show()