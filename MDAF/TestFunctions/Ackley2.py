import math as m

def main(args):

    '''
    #_# dimmensions: 2
	#_# upper: 32
	#_# lower: -32
	#_# minimum: [0, 0]

    >>> main([0, 0])
    -200.0

    '''
    return -200 * m.e**(-0.02 * m.sqrt(args[0]**2 + args[1]**2))