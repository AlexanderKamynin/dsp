import numpy as np
import matplotlib.pyplot as plt


class DeviationDistribution:
    # Calculate the deviation for signal
    def __init__(self, true_signal):
        self.__true_signal = true_signal
        self.__deviation_sequence = None
        self.__distribution_function = []

    def get_deviation_sequence(self, processed_signal):
        sequence_length = len(self.__true_signal)
        self.__deviation_sequence = np.zeros(sequence_length)

        for i in range(sequence_length):
            self.__deviation_sequence[i] = self.__true_signal[i] - processed_signal[i]

    def get_distribution_function(self):
        """ F(x) = P (X < x), where
            P (X < x) = count(X < x) / N where N - length of the signals sequence
        """
        sorted_deviation = self.__deviation_sequence.sort(axis=0)
        sequence_length = len(self.__true_signal)

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

    def plot_distribution_function(self):
        plt.figure(figsize=(16,8))
        plt.title('Distribution function')
        plt.xlabel('deviation - x')
        plt.ylabel('F(x)')
        plt.grid()

        plt.scatter(self.__distribution_function[:, 0], self.__distribution_function[:, 1])

        plt.savefig('./output/distribution.png')
