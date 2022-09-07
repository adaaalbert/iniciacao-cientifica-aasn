import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.stats import linregress
from kinetics_helpers import plot_params

plt.style.use('seaborn')
ureg = pint.UnitRegistry()
ureg.setup_matplotlib()


class Kinetics:

    def __init__(self, data_file):
        self.data = self._data_from_file(data_file)

    @staticmethod
    def _data_from_file(data_file):
        return np.genfromtxt(open(data_file), delimiter=',',
                             dtype=(float, float),
                             names=['T_min', 'Conc_molL'],
                             skip_header=1)

    @property
    def time(self):
        return self.data['T_min'] * ureg('min')

    @property
    def concentration(self):
        return self.data['Conc_molL'] * ureg('mol/l')

    @property
    def regression_conc(self):
        reg_conc = linregress(self.time.magnitude, self.concentration.magnitude)
        return reg_conc

    @property
    def regression_ln_conc(self):
        reg_ln_conc = linregress(self.time.magnitude,
                                 np.log(self.concentration.magnitude))
        return reg_ln_conc

    @property
    def regression_inv_conc(self):
        reg_inv_conc = linregress(self.time.magnitude,
                                  (1 / self.concentration.magnitude))
        return reg_inv_conc

    @property
    def linear_fit_conc(self):
        x = np.linspace(self.time[0].magnitude,
                        self.time[-1].magnitude, 50)
        y_conc = self.regression_conc.slope * x + self.regression_conc.intercept
        return x, y_conc

    @property
    def linear_fit_ln_conc(self):
        x = np.linspace(self.time[0].magnitude, self.time[-1].magnitude, 50)
        y_ln_conc = self.regression_ln_conc.slope * x + self.regression_ln_conc.intercept
        return x, y_ln_conc

    @property
    def linear_fit_inv_conc(self):
        x = np.linspace(self.time[0].magnitude,
                        self.time[-1].magnitude, 50)
        y_inv_conc = self.regression_inv_conc.slope * x + self.regression_inv_conc.intercept
        return x, y_inv_conc

    @property
    def rate_constant(self):
        return abs(self.regression_ln_conc.slope)

    def plot(self):
        fig, axs = plt.subplots(figsize=(8, 6), nrows=2, ncols=2, tight_layout=True)

        # Concentration vs time
        plot_params(axs.flat[0])
        axs.flat[0].scatter(self.time.magnitude, self.concentration.magnitude, c='b')
        axs.flat[0].plot(*self.linear_fit_conc, color='red')
        # Log (conc) vs time
        plot_params(axs.flat[1])
        axs.flat[1].scatter(self.time.magnitude, np.log(self.concentration.magnitude))
        axs.flat[1].plot(*self.linear_fit_ln_conc, color='red')
        # 1 / Conc. vs time
        plot_params(axs.flat[2])
        axs.flat[2].scatter(self.time.magnitude, 1 / self.concentration.magnitude)
        axs.flat[2].plot(*self.linear_fit_inv_conc, color='red')

        plt.show()


if __name__ == '__main__':
    file = 'dados.csv'
    kinetics = Kinetics(file)
    kinetics.plot()
    print(kinetics.rate_constant)
