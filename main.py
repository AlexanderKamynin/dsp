import numpy as np
import matplotlib.pyplot as plt
from src.generator.signal_generator import SignalGenerator
from src.filter.filter import Filter
from src.distribution.distribution import DeviationDistribution
from src.autocorrelation.autocorrelation import AutocorrelationFunction


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
        self.__signal_sequence = None
        self.__deviation_distribution = None
        self.__autocorrelation_function = None

    def start(self):
        # args = list(map(float, input('Input the amplitude, frequency and phase for harmonic signal:\n').split()))
        args = [3, 1, 1]
        self.__signal_generator = SignalGenerator(*args)

        # args = list(map(float, input('Input the start time, count of discrete dots and step:\n').split()))
        args = [0, 1000, 0.1]
        self.__signal_sequence = self.__signal_generator.generate_noise_signal(*args)
        self.plot_signal(self.__signal_sequence)

        # TODO: add the choice for filtering method (now it's one, but in future we can add more)
        # args = list(map(float, input('Input the window size time:\n').split()))
        args = [15]
        self.__filter = Filter(*args)
        filtered_signal = self.__filter.filter(self.__signal_sequence)
        self.plot_signal(filtered_signal, title="filtered_signal")

        self.__deviation_distribution = DeviationDistribution(self.__signal_sequence)
        self.__deviation_distribution.get_deviation_sequence(filtered_signal)
        self.__deviation_distribution.get_distribution_function()
        self.__deviation_distribution.plot_distribution_function()

        self.__autocorrelation_function = AutocorrelationFunction(self.__signal_sequence,
                                                                  self.__signal_generator.get_parameters()['time'])
        self.__autocorrelation_function.ring_shift()
        self.__autocorrelation_function.plot_autocorrelation_function()

    def plot_signal(self, signal_seq, title="generated_signal"):
        # if not self.__signal_sequence.any():
        #  raise NameError("You don't create the signal sequence")

        plt.figure(figsize=(16,8))
        plt.title(title)
        plt.xlabel('time')
        plt.ylabel('signal value')
        plt.grid()

        param = self.__signal_generator.get_parameters()
        plt.plot(param['time'], signal_seq,
                 label=f"A = {param['amplitude']}, w = {param['frequency']}, phi0 = {param['phase']}")
        plt.legend(loc='upper right')

        plt.savefig(f"./output/{title}.png")



if __name__ == '__main__':
    dsp = DigitalSignalProcessing()
    dsp.start()


