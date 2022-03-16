from typing import List, Callable
import json
class Signal:
   def __init__(self, amplitude: float, signal_start_time: float, signal_duration: float, frequency: int, type_of_signal: Callable):
      self.signal_start_time = signal_start_time
      self.signal_duration = signal_duration
      self.frequency = frequency
      self.samples, self.values = type_of_signal(amplitude, signal_duration, frequency, signal_start_time)
      self.name = type_of_signal.__name__

   def save_to_file(self):
      name = "".join([str(elem) for elem in self.name.split("_")[1:]]) + ".json"
      output = open(name, "w")
      signal_dict = {
         "signal_start_time": self.signal_start_time,
         "signal_duration": self.signal_duration,
         "frequency": self.frequency,
         "samples": self.samples,
         "values": self.values,
      }
      json.dump(signal_dict, output, indent=6)
      output.close()