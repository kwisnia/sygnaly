import functions as fn
from Signal import Signal
from plot import plot


if __name__ == "__main__":
    newsignal = Signal(3.0, 0, 5, 50, fn.generate_gauss_noise)
    plot(newsignal)
    fn.save_to_file(newsignal)
    signal = fn.load_from_file("gaussnoise.json")
    plot(signal)
