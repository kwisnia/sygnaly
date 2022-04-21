import matplotlib.pyplot as plt

def zero_order_hold(original_signal):
   plt.step(original_signal.samples, [original_signal.values[i] for i in range(len(original_signal.samples))])
   plt.show()