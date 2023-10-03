from src.generator.signal_generator import SignalGenerator
from src.filter.filter import Filter
from src.distribution.distribution import DeviationDistribution
from src.autocorrelation.autocorrelation import AutocorrelationFunction
from src.plotter.plotter import Plotter


class DigitalSignalProcessing:
    def __init__(self):
        self.__signal_sequence = None

        self.__signal_generator = None
        self.__filter = None
        self.__deviation_distribution = None
        self.__autocorrelation_function = None

    def start(self):
        # args = list(map(float, input('Input the amplitude, frequency and phase for harmonic signal:\n').split()))
        args = [3, 1, 1]
        self.__signal_generator = SignalGenerator(*args)

        # args = list(map(float, input('Input the start time, count of discrete dots and step:\n').split()))
        args = [0, 1000, 0.1]
        self.__signal_sequence = self.__signal_generator.generate_noise_signal(*args)
        time = self.__signal_generator.get_parameters()['time']

        Plotter.plot_data(time, self.__signal_sequence,
                                 'Generated signal',
                                 'time',
                                 'x(t)',
                                 './output/generated_signal.png')

        # TODO: add the choice for filtering method (now it's one, but in future we can add more)
        # args = list(map(float, input('Input the window size time:\n').split()))
        args = [15]
        self.__filter = Filter(*args)
        filtered_signal = self.__filter.filter(self.__signal_sequence)
        Plotter.plot_data(time, filtered_signal,
                                 'Filtered signal',
                                 'time',
                                 'x(t)',
                                 './output/filtered_signal.png')


        self.__deviation_distribution = DeviationDistribution(self.__signal_sequence, filtered_signal)
        self.__deviation_distribution.calculate_distribution_function()
        distr_func = self.__deviation_distribution.get_distribution_function()
        Plotter.scatter_data(distr_func[:, 0], distr_func[:, 1],
                                    'Distribution function',
                                    'deviation x(t) - x_new(t)',
                                    'F(x)',
                                    './output/distribution.png')

        self.__autocorrelation_function = AutocorrelationFunction(self.__signal_sequence,
                                                                  self.__signal_generator.get_parameters()['time'])
        self.__autocorrelation_function.ring_shift()
        autocorr_func = self.__autocorrelation_function.get_autocorrelation_function()
        Plotter.scatter_data(time[:len(time) // 4], autocorr_func[:len(autocorr_func) // 4],
                                    'Autocorrelation function with Ring Shift',
                                    't',
                                    'R(t)',
                                    './output/autocorrelation.png'
                                    )


        self.__autocorrelation_function.fast_fourier_transform()
        autocorr_func = self.__autocorrelation_function.get_autocorrelation_function()
        Plotter.scatter_data(time[:len(time) // 4], autocorr_func[:len(autocorr_func) // 4],
                                    'Autocorrelation function with FFT',
                                    't',
                                    'R(t)',
                                    './output/autocorrelation_FFT.png'
                                    )

    def save_to_file(self, filename, title, line_description, *data):
      """ Method for saving the obtained data with following template:
          {
            Title
            Line format description
            Data
          }

          example:
          Source signal
          t | x(t)
          0 2
          1 4
          2 6
          . . .
      """
      # TODO:
      output_lines = []
      #file = open(filename, 'w')

      for column, data_sample in enumerate(data):
        for row, elem in enumerate(data_sample):
          output_lines[row][column] += str(elem) + ' '

      print(output_lines)
      #file.close()


if __name__ == '__main__':
    dsp = DigitalSignalProcessing()
    dsp.start()
    #time = [0, 1, 2, 3]
    #x = [2, 4, 6, 8]
    #dsp.save_to_file('./output/text.txt', 'test', 't | x(t)', time, x)