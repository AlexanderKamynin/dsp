import numpy as np


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

