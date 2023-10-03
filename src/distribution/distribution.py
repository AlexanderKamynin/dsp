import numpy as np
import matplotlib.pyplot as plt


class DeviationDistribution:
    # Calculate the deviation for signal
    def __init__(self, true_signal, processed_signal):
        self.__true_signal = true_signal
        self.__processed_signal = processed_signal
        self.__deviation_sequence = None
        self.__distribution_function = []

    def __calculate_deviation_sequence(self):
        sequence_length = len(self.__true_signal)
        self.__deviation_sequence = np.zeros(sequence_length)

        for i in range(sequence_length):
            self.__deviation_sequence[i] = self.__true_signal[i] - self.__processed_signal[i]

    def calculate_distribution_function(self):
        """ F(x) = P (X < x), where
            P (X < x) = count(X < x) / N where N - length of the signals sequence
        """
        self.__calculate_deviation_sequence()
        self.__deviation_sequence.sort(axis=0)

        sequence_length = len(self.__true_signal)

        self.__distribution_function.append([0, 0]);

        prev_deviation = self.__deviation_sequence[0]
        count = 1
        for i in range(1, sequence_length):
            current_deviation = self.__deviation_sequence[i]
            if current_deviation != prev_deviation:
                self.__distribution_function.append([prev_deviation, count / sequence_length])
            prev_deviation = current_deviation
            count += 1

        self.__distribution_function.append([prev_deviation, count / sequence_length])

        self.__distribution_function = np.array(self.__distribution_function)

    def get_distribution_function(self):
      return self.__distribution_function

