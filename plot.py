import matplotlib.pyplot as plt
from Signal import Signal

def plot(signal: Signal):
   plt.plot(signal.samples, signal.values)
   plt.show()