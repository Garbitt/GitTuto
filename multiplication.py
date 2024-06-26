def mult(x, y):
    """
    Commentaire pour la multiplication important
    :param x:
    :param y:
    :return:
    """
    if isinstance(x, type(y)):
        if isinstance(x, int):
            return mult_int(x, y)
        elif isinstance(x, float):
            return mult_float(x, y)
        else:
            return mult_other(x, y)
    else:
        t = type(x)
        y_t = t(y)
        return mult(x, y_t)


def mult_int(x: int, y: int) -> int:
    """
    :param x:
    :param y:
    :return:
    """
    return x * y


def mult_float(x: float, y: float) -> float:
    """
    :rtype: object
    :param x:
    :param y:
    :return:
    """
    return x * y


def mult_other(x, y) -> Exception | float:
    """
    :param x:
    :param y:
    :return:
    """
    try:
        x_float = float(x)
        y_float = float(y)
    except Exception as e:
        return e
    return mult_float(x_float, y_float)
