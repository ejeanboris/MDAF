
def main(args):
    '''
    >>> main([0,1])
    0.26

    
    #_# dimmensions: 2
	#_# upper: 10
	#_# lower: -10
	#_# minimum: [0, 0]
    '''
    for x in args:
        if x < -10 or x > 10:
            return 0
    return (0.26*(args[0]**2+args[1]**2))-(0.48*args[0]*args[1])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
