import matplotlib.pyplot as plt
import numpy as np


def zero_order_hold(original_signal):
   plt.step(original_signal.samples, [original_signal.values[i] for i in range(len(original_signal.samples))])
   plt.show()


def first_order_hold(original_signal):
   plt.plot(original_signal.samples, [original_signal.values[i] for i in range(len(original_signal.samples))])
   plt.show()


def sinc(original_signal):
   plt.plot(original_signal.samples, np.sinc(original_signal.values))
   plt.show()