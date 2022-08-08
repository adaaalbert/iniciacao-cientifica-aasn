import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

# GAS_CONSTANT = Q_(8.314462618, 'J/(K * mol)')
GAS_CONSTANT = Q_(0.082057366080960, 'atm * l / (mol * K)')


@ureg.wraps('liter/mol', ('K', 'atm'))
def perfect_gas_volume(temperature, pressure):
    """
    Parameters
    ----------
    temperature
    pressure

    Returns
    -------

    """

    return GAS_CONSTANT.magnitude * temperature / pressure


if __name__ == '__main__':
    print(perfect_gas_volume('273 K', '1 atm'))
