import math


def rectangular_window():
   return 1.0


def blackman_window(M: int, number_of_sample: int):
   return 0.42 - 0.5 * math.cos(2 * math.pi * number_of_sample / M) + 0.08 * math.cos(4 * math.pi * number_of_sample / M)