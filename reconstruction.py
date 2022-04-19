import matplotlib.pyplot as plt

def zero_order_hold(original_signal, quantization_threshold):
   plt.step(original_signal.samples, [original_signal.values[i] + quantization_threshold for i in range(len(original_signal.samples))])
   plt.show()