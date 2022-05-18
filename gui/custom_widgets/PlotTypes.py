from enum import Enum

class PlotTypes(Enum):
    """
    Enum for the different plot types
    """
    LINE = 1
    HISTOGRAM = 2
    SCATTER = 3
    STEM = 4
    STEP = 5