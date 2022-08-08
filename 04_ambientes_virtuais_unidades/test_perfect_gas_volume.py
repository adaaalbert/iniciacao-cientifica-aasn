from perfect_gas_volume import perfect_gas_volume, Q_
import numpy as np


def test_gas_volume_cntp():
    temperature = Q_(273, 'K')
    pressure = Q_(1, 'atm')
    expected_volume = Q_(22.40, 'liter/mol')
    assert np.isclose(perfect_gas_volume(temperature, pressure),
                      expected_volume, atol=0.1)


def test_gas_volume_catp():
    temperature = Q_(298, 'K')
    pressure = Q_(1, 'atm')
    expected_volume = Q_(24.45, 'liter/mol')
    assert np.isclose(perfect_gas_volume(temperature, pressure),
                      expected_volume, atol=0.01)