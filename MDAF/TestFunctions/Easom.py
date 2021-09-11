import math

def main(args):
    '''
    >>> (main([3.1415,3.1415]) + 1) < 0.001
    True

    
    #_# dimmensions: 2
	#_# upper: 100
	#_# lower: -100
	#_# minimum: [3.1415, 3.1415]
    #_# opti: -1
    '''
    return -1*math.cos(args[0])*math.cos(args[1])*math.exp(-(args[0]-math.pi)**2-(args[1]-math.pi)**2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
