from typing import list, Callable
class Signal:
   def __init__(self, amplitude: float, start: float, length: float, type: Callable):
      self.amplitude = amplitude
      self.start = start
      self.length = length
   FREQUENCY = 50

