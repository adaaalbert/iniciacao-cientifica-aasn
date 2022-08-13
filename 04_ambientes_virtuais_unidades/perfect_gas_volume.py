import pint
from scipy.constants import gas_constant

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# GAS_CONSTANT = Q_(8.314462618, 'J/(K * mol)')
#GAS_CONSTANT = Q_(0.082057366080960, 'atm * l / (mol * K)')
gas_constant = gas_constant * ureg('(m**3 * Pa)/(K*mol)')

# @ureg.wraps('liter/mol', ('K', 'atm'))
@ureg.wraps('liter/mol', ('K', 'Pa'))
def perfect_gas_volume(temperature, pressure):
    """
    Parameters
    ----------
    temperature
    pressure

    Returns
    -------

    """

    return gas_constant.magnitude * temperature / pressure


if __name__ == '__main__':
    # print(perfect_gas_volume('273 K', '1 atm'))
    print(perfect_gas_volume('273 K', '101325 Pa'))