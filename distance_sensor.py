import operator

class DistanceSensor():
   def __init__(self, probe_signal_period, sample_rate, buffer_len, report_period) -> None:
      self.probe_signal_period = probe_signal_period
      self.sample_rate = sample_rate
      self.buffer_len = buffer_len
      self.report_period = report_period
      self.calculation_timestamp = float("-inf")
      self.distance = 0

   def generate_probing_signal(self):
      # wygeneruj dwa sygnaly i je dodaj
      pass

   def update(self, feedback_signal, timestamp):
      start_time = timestamp - self.buffer_len / self.sample_rate
      # wyznacz wartosci sygnalu probujacego
      # wyznacz wartosci sygnalu zwrotnego

      if ((timestamp - self.calculation_timestamp) >= self.report_period):
         self.calculation_timestamp = timestamp
         self.calculate_distance()
   

   def calculate_distance(self, signal_velocity):
      # skoreluj sygnal zwrotny z przeszukujacym
      index, value = max(enumerate(correlation_signal.values[:len(correlation_signal.values) / 2]), key=operator.itemgetter(1))

      delay = index / self.sample_rate
      self.distance = delay * signal_velocity / 2.0