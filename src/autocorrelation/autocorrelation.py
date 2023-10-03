import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft


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

    def fast_fourier_transform(self):
      """
        Autocorrelation function with using FFT (Fast Fourier Transform)
        R(t)=Re[IFFT(|FFT(x)|^2)], where:
          FFT - forward fast Fourier transform,
          IFFT - inverse fast Fourier transform,
          Re - real part of the complex number
      """
      # FFT(x)
      calculation_result = fft(self.__signal_sequence)

      # |FFT(x)|^2 = (sqrt(Re(x)^2 + Im(x)^2))^2 = Re(x)^2 + Im(x)^2
      calculation_result = calculation_result.real ** 2 + calculation_result.imag ** 2

      # Re[IFFT(|FFT(x)|^2)]
      calculation_result = ifft(calculation_result).real

      """
        The result of the FFT returns C * R(t).
        It is known that for the first element the correlation coefficient is equal to 1.
        Then the coefficient C can be easily expressed as 1/R(0).
      """
      self.__autocorrelation_sequence = calculation_result / calculation_result[0]

    def get_autocorrelation_function(self):
      return self.__autocorrelation_sequence

