import numpy as np
import matplotlib.pyplot as plt
import pint
from scipy.stats import linregress
from kinetics_helpers import plot_params


ureg = pint.UnitRegistry
ureg.setup_matplotlib()


class Kinetics:

    def __init__(self, data_file):
        self.data = self._data_from_file(data_file)

    @staticmethod
    def _data_from_file(data_file):
        return np.genfromtxt(open(data_file), delimiter=',',
                             dtype=(float, float),
                             names=['T_min', 'Conc_mol/L'], skip_header=1)

    @property
    def concentration_data(self):
        return self.data['Conc_mol/L'] * ureg('mol/L')

    @property
    def time_data(self):
        return self.data['T_min'] * ureg.min

    @property
    def regression(self):


if __name__ == '__main__':
    file = 'dados.csv'
