import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

GAS_CONSTANT = Q_(0.082057366080960, 'atm * l / (mol * K)')


@ureg.wraps('liter/mol', ('atm * dm**6 / mol**2', 'dm**3 / mol', 'K', 'atm'))
def van_der_waals(a, b, temperature, pressure):
    """

    Parameters
    ----------
    a
        van der Waals coefficient - attractive interacitons / 
        ('atm * dm**6 / mol**2')
    b
        van der Waals coefficient - repulsive interactions / 
        ('dm**3 / mol')
    temperature
        temperature of the gas / K


    Returns
    -------
    returns the real root of the soluttion of van der Waals equation cubic form
    """
    coef_V3 = 1
    coef_V2 = -(b + GAS_CONSTANT.magnitude * temperature / pressure)
    coef_V1 = a / pressure
    coef_V0 = - a * b / pressure
    poly = np.polynomial.Polynomial((coef_V0, coef_V1, coef_V2, coef_V3))
    roots = poly.roots()

    return roots[np.isreal(roots)]
