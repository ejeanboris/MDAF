import math


def main(args):
    """
    >>>main([0, 1, 1, 1])
    0
    :param args:
    :return:
    """
    for x in args:
        if x < -1 or x > 1:
            return 0
    return (math.exp(-args[0])-args[1])**4+(100*(args[1]-args[2])**6)+(math.tan(args[2]-args[3]))**4+args[0]**8


