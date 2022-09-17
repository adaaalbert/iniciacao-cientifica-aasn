from itertools import cycle
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import pint
from scipy.stats import linregress
from helpers import plot_params

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
    def _regression_conc(self):
        reg_conc = linregress(self.time.magnitude, self.concentration.magnitude)
        return reg_conc

    @property
    def _regression_ln_conc(self):
        reg_ln_conc = linregress(self.time.magnitude,
                                 np.log(self.concentration.magnitude))
        return reg_ln_conc

    @property
    def _regression_inv_conc(self):
        reg_inv_conc = linregress(self.time.magnitude,
                                  (1 / self.concentration.magnitude))
        return reg_inv_conc

    @property
    def _linear_fit_conc(self):
        x = np.linspace(self.time[0].magnitude,
                        self.time[-1].magnitude, 50)
        y_conc = self._regression_conc.slope * x + self._regression_conc.intercept
        return x, y_conc

    @property
    def _linear_fit_ln_conc(self):
        x = np.linspace(self.time[0].magnitude, self.time[-1].magnitude, 50)
        y_ln_conc = self._regression_ln_conc.slope * x + self._regression_ln_conc.intercept
        return x, y_ln_conc

    @property
    def _linear_fit_inv_conc(self):
        x = np.linspace(self.time[0].magnitude,
                        self.time[-1].magnitude, 50)
        y_inv_conc = self._regression_inv_conc.slope * x + self._regression_inv_conc.intercept
        return x, y_inv_conc

    @property
    def order(self):
        r2 = [self._regression_conc.rvalue ** 2,
              self._regression_ln_conc.rvalue ** 2,
              self._regression_inv_conc.rvalue ** 2]
        return np.argmax(r2)

    @property
    def rate_constant(self):
        if self.order == 0:
            return abs(self._regression_conc.slope)
        elif self.order == 1:
            return abs(self._regression_ln_conc.slope)
        elif self.order == 2:
            return abs(self._regression_inv_conc.slope)
        else:
            raise ValueError("Undefined order")

    def _plot_matplotlib(self):
        fig, axs = plt.subplots(figsize=(8, 6), nrows=2, ncols=2, tight_layout=True)

        # Concentration vs time
        plot_params(axs.flat[0])
        axs.flat[0].scatter(self.time.magnitude, self.concentration.magnitude, c='b')
        axs.flat[0].plot(*self._linear_fit_conc, color='red')
        # Log (conc) vs time
        plot_params(axs.flat[1])
        axs.flat[1].scatter(self.time.magnitude, np.log(self.concentration.magnitude))
        axs.flat[1].plot(*self._linear_fit_ln_conc, color='red')
        # 1 / Conc. vs time
        plot_params(axs.flat[2])
        axs.flat[2].scatter(self.time.magnitude, 1 / self.concentration.magnitude)
        axs.flat[2].plot(*self._linear_fit_inv_conc, color='red')

        plt.show()

    def _plot_plotly(self):
        fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                            # subplot_titles=("Conc vs Time",
                            #                 "Log(conc) vs Time",
                            #                 "1/Conc vs Time"),
                            start_cell="top-left")

        # Plot concentration & _linear_fit_concentration
        fig.add_trace(go.Scatter(x=self.time.magnitude,
                                 y=self.concentration.magnitude,
                                 mode='markers',
                                 name='Conc (mol/L)',
                                 marker=dict(size=10),
                                 hovertemplate="%{x:.2f}, %{y:.4f}", legendgroup=1),
                      row=1, col=1)

        fig.add_trace(go.Scatter(x=self._linear_fit_conc[0],
                                 y=self._linear_fit_conc[1],
                                 mode='lines',
                                 name='Linear fit 1',
                                 hovertemplate="%{x:.2f}, %{y:.4f}", legendgroup=1),
                      row=1, col=1)

        # Plot log(conc) & _linear_fit_ln_conc
        palette = cycle(px.colors.qualitative.Plotly)
        fig.add_trace(go.Scatter(x=self.time.magnitude,
                                 y=np.log(self.concentration.magnitude),
                                 mode='markers',
                                 name='Log (Conc)',
                                 marker=dict(size=10, color=next(palette)),
                                 hovertemplate="%{x:.2f}, %{y:.4f}", legendgroup=2),
                      row=2, col=1)
        fig.add_trace(go.Scatter(x=self._linear_fit_ln_conc[0],
                                 y=self._linear_fit_ln_conc[1],
                                 mode='lines',
                                 name='Linear fit 2',
                                 line=dict(color=next(palette)),
                                 hovertemplate="%{x:.2f}, %{y:.4f}", legendgroup=2),
                      row=2, col=1)

        # Plot 1 / conc & _linear_fit_inv_conc
        palette = cycle(px.colors.qualitative.Plotly)
        fig.add_trace(go.Scatter(x=self.time,
                                 y=1 / self.concentration.magnitude,
                                 mode='markers',
                                 name='1/Conc (L/mol)',
                                 marker=dict(size=10, color=next(palette)),
                                 hovertemplate="%{x:.2f}, %{y:.4f}", legendgroup=3),
                      row=3, col=1)
        fig.add_trace(go.Scatter(x=self._linear_fit_inv_conc[0],
                                 y=self._linear_fit_inv_conc[1],
                                 mode='lines',
                                 name='Linear fit 3',
                                 line=dict(color=next(palette)),
                                 hovertemplate="%{x:.2f}, %{y:.4f}", legendgroup=3),
                      row=3, col=1)

        # TODO reset color cycle e outras padronizações dos gráficos
        fig.update_layout(hovermode='closest')
        fig.update_xaxes(showspikes=True)
        fig.update_yaxes(showspikes=True)
        fig.update_layout(
            font={'size': 12},
            # template='plotly_dark',
            xaxis3_tickformat='.1f',
            yaxis3_tickformat='.1f',
            legend_tracegroupgap=120,
            width=600
        )
        fig['layout']['yaxis']['title'] = r'$[A] / \text{mol} \cdot \ell^{-1} $'
        fig['layout']['yaxis2']['title'] = r'$\ln [A]$'
        fig['layout']['yaxis3']['title'] = r'$\frac{1}{[A]} / \ell \cdot \text{mol}^{-1}$'

        fig.update_xaxes(title_text="Tempo / min", row=3)

        fig.add_annotation(x=10, y=0.8,
                           text=f'y = {self._regression_conc.slope:.3e}x + '
                                f'{self._regression_conc.intercept:.3e}',  # NOQA
                           xref='paper', yref='paper', showarrow=False,
                           font=dict(color='white'), bgcolor='red',
                           opacity=0.8, row=1, col=1)

        fig.add_annotation(x=10, y=0,
                           text=f'y = {self._regression_ln_conc.slope:.3e}x + '
                                f'{self._regression_ln_conc.intercept:.3e}',  # NOQA
                           xref='paper', yref='paper', showarrow=False,
                           font=dict(color='white'), bgcolor='green',
                           opacity=0.8, row=2, col=1)

        fig.add_annotation(x=5, y=30,
                           text=f'y = {self._regression_inv_conc.slope:.3e}x + '
                                f'{self._regression_inv_conc.intercept:.3e}',  # NOQA
                           xref='paper', yref='paper', showarrow=False,
                           font=dict(color='white'), bgcolor='blue',
                           opacity=0.8, row=3, col=1)

        # fig.show()
        fig.write_html('output.html', auto_open=True, include_mathjax='cdn')

    def plot(self, backend='matplotlib'):
        if backend == 'matplotlib':
            self._plot_matplotlib()
        elif backend == 'plotly':
            self._plot_plotly()
        else:
            raise ValueError('Invalid plot backend')


if __name__ == '__main__':
    file = 'dados.csv'
    kinetics = Kinetics(file)
    print(kinetics.order)
    print(kinetics.rate_constant)
    kinetics.plot('plotly')
