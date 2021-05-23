from math import sqrt, fabs


def main(args):
    '''
    #_# dimmensions: 2
	#_# upper: [-5, 3]
	#_# lower: [-15, -3]
	#_# minimum: [-10,1]
    
	'''
    return 100*sqrt(fabs(args[1]-0.01*args[0]**2))+0.01*fabs(args[0]+10)
