from Signal import Signal
import numpy as np
from copy import deepcopy


def add(first: Signal, second: Signal):
   if (len(first.samples) == len(second.samples)):
      new_signal = deepcopy(first)
      new_signal.values = list(np.add(first.values, second.values))
      return new_signal
   return False


def subtract(first: Signal, second: Signal):
   if (len(first.samples) == len(second.samples)):
      new_signal = deepcopy(first)
      new_signal.values = list(np.subtract(first.values, second.values))
      return new_signal
   return False


def multiply(first: Signal, second: Signal):
   if (len(first.samples) == len(second.samples)):
      new_signal = deepcopy(first)
      new_signal.values = list(np.multiply(first.values, second.values))
      return new_signal
   return False


def divide(first: Signal, second: Signal):
   if (len(first.samples) == len(second.samples)):
      new_signal = deepcopy(first)
      #new_signal.values = np.divide(first.values, second.values, out=np.zeros_like(first.values), where=second.values!=0)
      new_signal.values = list(f_sample / s_sample if s_sample != 0 else f_sample for f_sample, s_sample in zip(first.values, second.values))
      return new_signal
   return False

def convolve(first: Signal, second: Signal):
   new_signal = deepcopy(first)
   new_signal.values = list(np.convolve(first.values, second.values))
   return new_signal