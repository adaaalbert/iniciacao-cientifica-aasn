import pint


ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

ureg.wraps('meter', 'second')


def avg_speed(distance, time):
    """
    Returns the average speed by dividing distance by time.

    Parameters
    ----------
    distance : float
        Description:

    time : float
        Desc:

    Returns
    -------
    float
        Desc:

    """

    return distance / time
