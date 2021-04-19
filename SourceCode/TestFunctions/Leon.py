#Import math library


def main(args):
    for x in args:
        if x < -1.2 or x > 1.2:
            return 0
    return (100*(args[1]-args[0])**2)+(1-args[0])**2
