import numpy as np
import matplotlib.pyplot as plt


class SignalGenerator:
    def __init__(self, amplitude: float, frequency: float, phase: float):
        self.__amplitude = amplitude
        self.__frequency = frequency
        self.__phase = phase
        self.__time = None

    def generate_signal(self, start_time: float, count: float, step: float):
        self.__time = np.linspace(start_time, start_time + count * step, int(count))
        # x(t) = A * sin(wt + phi0)
        x = self.__amplitude * np.sin(self.__frequency * self.__time + self.__phase)
        return x

    def generate_noise_signal(self, start_time: float, count:int, step: float):
        x = self.generate_signal(start_time, count, step)
        # add the noise
        noise = np.random.randn(count) # random noise with normal distribution
        # x(t) = x(t) + noise
        return x + noise

    def get_parameters(self):
        return {
            'amplitude': self.__amplitude,
            'frequency': self.__frequency,
            'phase': self.__phase,
            'time': self.__time
        }


class Filter:
    def __init__(self, window_size):
        self.__window_size = window_size

    def filter(self, signal_sequency):
        seq_length = len(signal_sequency)
        filtered_signal = np.zeros(seq_length)

        if self.__window_size > seq_length:
            raise NameError("Window size greater signal sequency length")

        if self.__window_size % 2 == 0: # if even, increase the window size for one center
            self.__window_size += 1

        half_w_size = (self.__window_size - 1) // 2

        filtered_signal[0] = signal_sequency[0]
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
                cur_window = [2*i-seq_length+1, seq_length-1]
                cur_window.append(cur_window[1] - cur_window[0] + 1)
            else:
                cur_window = [i-half_w_size, i+half_w_size, self.__window_size]

            # compute the new x
            for j in range(cur_window[0], cur_window[1] + 1):
                window_sum += signal_sequency[j]

            filtered_signal[i] = window_sum / cur_window[2]

        return filtered_signal


class DigitalSignalProcessing:
    # Постановка задачи:

    # 1.    Реализовать программный модуль фильтрации входящего сигнала на основе скользящего окна;
    # 2.    Найти временной ряд отклонений (дисперсий) и построить их функцию распределения;
    # 3.    Построить автокорреляционную функцию временного ряда:
    # •   Реализовать при помощи стандартного способа (кольцевого смещения);
    # •   При помощи БПФ;
    def __init__(self):
        self.__signal_generator = None
        self.__filter = None
        self.__signal_sequency = None

    def start(self):
        # args = list(map(float, input('Input the amplitude, frequency and phase for garmonical signal:\n').split()))
        args = [3, 1, 1]
        self.__signal_generator = SignalGenerator(*args)

        # args = list(map(float, input('Input the start time, count of disrete dots and step:\n').split()))
        args = [0, 1000, 0.1]
        self.__signal_sequency = self.__signal_generator.generate_noise_signal(*args)
        self.plot_signal(self.__signal_sequency)

        # TODO: add the choice for filtering method (now it's one, but in future we can add more)
        # args = list(map(float, input('Input the window size time:\n').split()))
        args = [15]
        self.__filter = Filter(*args)
        filtered_signal = self.__filter.filter(self.__signal_sequency)
        self.plot_signal(filtered_signal, title="Filtered signal")

    def plot_signal(self, signal_seq, title="Generated signal"):
        # if not self.__signal_sequency.any():
        #  raise NameError("You don't create the signal sequency")

        plt.figure(figsize=(8,8))
        plt.title(title)
        plt.xlabel('time')
        plt.ylabel('signal value')
        plt.grid()

        param = self.__signal_generator.get_parameters()
        plt.plot(param['time'], signal_seq, \
            label=f"A = {param['amplitude']}, w = {param['frequency']}, phi0 = {param['phase']}")
        plt.legend(loc='upper right')

        plt.show()



if __name__ == '__main__':
    dsp = DigitalSignalProcessing()
    dsp.start()


