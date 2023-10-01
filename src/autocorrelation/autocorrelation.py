import numpy as np
import matplotlib.pyplot as plt


class AutocorrelationFunction:
    """
    Построить автокорреляционную функцию временного ряда:
    1) Реализовать при помощи стандартного способа (кольцевого смещения);
    2) При помощи БПФ;
    """
    def __init__(self, signal_sequence, time):
        self.__signal_sequence = signal_sequence
        self.__time = time
        self.__autocorrelation_sequence = np.zeros(len(self.__signal_sequence))

    def ring_shift(self):
        """ R(t) = corr(X(t), X(t+k)), where
            k - lag (shift) is integer number;

            the following formula is convenient for calculation
            corr(x,y) = (mean(x*y) - mean(x) * mean(y)) / sqrt(D(x) * D(y))
        """
        sequence_length = len(self.__signal_sequence)
        for lag in range(sequence_length // 4):
            original_sequence = self.__signal_sequence[:sequence_length-lag]
            shifted_sequence = self.__signal_sequence[lag:]

            mean_original = original_sequence.mean()
            mean_shifted = shifted_sequence.mean()

            mean_product = 0
            for i in range(len(original_sequence)):
                mean_product += original_sequence[i] * shifted_sequence[i]
            mean_product /= sequence_length - lag

            original_std = original_sequence.std()
            shifted_std = shifted_sequence.std()
            self.__autocorrelation_sequence[lag] = (mean_product - mean_original * mean_shifted) / (original_std * shifted_std)

    def plot_autocorrelation_function(self):
        plt.figure(figsize=(16,8))
        plt.title('Autocorrelation function')
        plt.xlabel('t')
        plt.ylabel('R(t)')
        plt.grid()

        plt.scatter(self.__time[:len(self.__time) // 4],
                    self.__autocorrelation_sequence[:len(self.__autocorrelation_sequence) // 4])
        plt.savefig('./output/autocorrelation.png')



