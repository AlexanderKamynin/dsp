class CLI:
    @staticmethod
    def choose_generator() -> dict:
        """
        :return: the dictionary with following key: ['generator_type', 'param', 'time']
        """
        args = dict()
        generator_type = [1, 2]
        args['generator_type'] = int(input("Choose the generator type:\n \
                                        1) Standard harmonical signals generator: A * sin(wt + phi0)\n \
                                        2) Harmonical signals generator with noise: A * sin(wt + phi0) + noise\n")
                                     )
        if args['generator_type'] not in generator_type:
            print('Chosen the default signals generator: 2')
            args['generator_type'] = 2

        args['param'] = list(map(float, input('Input the amplitude, frequency and phase for harmonic signal:\n').split()))
        args['time'] = list(map(float, input('Input the start time, count of discrete dots and step:\n').split()))

        return args

    @staticmethod
    def choose_autocorrelation_func() -> int:
        autocorrelation_type = [1, 2]
        args = int(input("Choose the autocorrelation function calculation method:\n \
                         1) Ring shift method\n \
                         2) FFT (Fast Fourier transform) method\n")
                  )
        if args not in autocorrelation_type:
            print('Chosen the default autocorrelation method')
            args = 2

        return args

    @staticmethod
    def input_window_size() -> int:
        """

        :return: the size for the filtering window
        """
        return int(input('Input the window size time:\n'))
