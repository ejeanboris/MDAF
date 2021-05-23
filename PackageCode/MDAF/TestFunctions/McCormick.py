import math
def main(args):
    '''
    >>>main([-0.547, -1.547])
    0
    
     #_# dimmensions: 2
    
    '''
    for args[0] in args:
        if args[0] < -1.5 or args[0] > 4:
            return 0
        if args[1] < -3 or args[1] > 3:
            return 0
    return math.sin(args[0]+args[1])+(args[0]-args[1])**2-(3*args[0]/2)+(5*args[1]/2)+1

