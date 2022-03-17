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
      new_signal.values = list(np.divide(first.values, second.values))
      return new_signal
   return False
