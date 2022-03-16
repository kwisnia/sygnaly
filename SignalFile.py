from Signal import Signal
class SignalFile(Signal): 
   def __init__(self, signal_dict: dict):
    self.signal_start_time = signal_dict['signal_start_time']
    self.signal_duration = signal_dict['signal_duration']
    self.frequency = signal_dict['frequency']
    self.samples = signal_dict['samples']
    self.values = signal_dict['values']
    self.name = signal_dict['name']
    self.fullfilment = signal_dict['fullfilment']
