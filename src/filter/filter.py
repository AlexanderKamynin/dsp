import numpy as np


class Filter:
    """
      Filter for given signal
    """
    def __init__(self, window_size: int):
        self.__window_size = window_size

    def filter(self, signal_sequence: np.ndarray) -> np.ndarray:
        """
          Method for filtering signals sequence using SMA (Simple Moving Average)
        """
        seq_length = len(signal_sequence)
        filtered_signal = np.zeros(seq_length)

        if self.__window_size > seq_length:
            raise NameError("Window size greater signal sequence length")

        if self.__window_size % 2 == 0: # if even, increase the window size for one center
            self.__window_size += 1

        half_w_size = (self.__window_size - 1) // 2

        filtered_signal[0] = signal_sequence[0]
        for i in range(1, seq_length):
            window_sum = 0
            cur_window = [] # list of numbers: start index window, end index window, size
            if i <= half_w_size: # begin of the sequence
                cur_window = [0, 2*i, 2*i+1]
            elif i + half_w_size > seq_length - 1: # end of the sequence
                ''' start: |--------[---i---]|
                    let i be the center of the window, so index for start of the window:
                    i - (N - i - 1) = 2i - N + 1
                    end: the end of the sequence
                    length: (end - start) + 1
                '''
                cur_window = [2 * i - seq_length + 1, seq_length - 1]
                cur_window.append(cur_window[1] - cur_window[0] + 1)
            else:
                cur_window = [i-half_w_size, i+half_w_size, self.__window_size]

            # compute the new x
            for j in range(cur_window[0], cur_window[1] + 1):
                window_sum += signal_sequence[j]

            filtered_signal[i] = window_sum / cur_window[2]

        return filtered_signal