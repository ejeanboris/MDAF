def main(args):
    result = 0
    for i,x in enumerate(args[1:-1]):
        result += (x**2)**(args[i+1]**2+1) + (args[i+1]**2)**(x**2 + 1)

    return result