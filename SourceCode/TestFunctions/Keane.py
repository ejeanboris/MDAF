#Import math library
import math


def main(args):
    for x in args:
        if(x<0 | x>10): return 0
    return (math.sin(args[0]-args[1])**2*math.sin(args[0]+args[1])**2)/(math.sqrt(args[0]**2+args[1]**2))
