import math as m
import numpy as np
from numpy import random as r
import time
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import copy as cp


#def func(Sc):
#    x1 = Sc[0]
#    x2 = Sc[1]
#    return m.sqrt(x1**2+x2**2)

def tweak(St,p,sigma,high,low):
    for i in range(len(St)):
        if p > r.random():
            while True:
                n = r.normal(loc=0, scale=sigma)
                if (high > St[i]+n) and (low < St[i]+n):
                    St[i]+=n
                    break
    return St

def Quality(Sc,objective,func):
    func_output = func(Sc)
    if type(func_output) == list:
        error = [func_output[i]-objective[i] for i in range(len(func_output))]
    else:
        error = func_output - objective
        #print("Error is: "+str(error))
    return 1/abs(error)

def main(func, S, args):
    r.seed(int(time.time()))
    route = list()
    #Parsing arguments
    y = args["objs"]
    t = args["t"]
    p = args["p"]
    high = max([args["upper"]])
    low = max([args["lower"]])
    
    Best = list()
    Best[:] = cp.deepcopy(S)
    sigma = 0.1
    route.append(Best[:])
    for iterationstep in range(100000):
        print('\n\n\n')
        R = tweak(cp.deepcopy(S),p,sigma,high, low)
        #print(R)
        #print(S)
        Qr = Quality(R,y,func)
        Qs = Quality(S,y,func)
        try:
            P = m.e**((Qr-Qs)/t)
        except:
            pass
        #print('QUALITY_R///{}'.format(Qr))
        #print('QUALITY_S///{}'.format(Qs))
        #print('fraction is:{}'.format(P))
        if (Qr > Qs) or (r.random() < P):
            #print('NEW_S')
            S[:] = R[:]
        if t > 0.01:
            t-= t/10
        #print('t = {}'.format(t))
        
        if (Quality(S,y,func) > Quality(Best,y,func)):
            #print('new Best****:{}'.format(Best))
            Best[:] = S[:]
            route.append(Best[:])
            #print(route)
            
        if t < 0 or Quality(Best,y,func) > 50:
            break
    #print('the Best Quality obtained was:{}'.format(Quality(Best,y)))
    #print("Final Quality is: {}".format(Quality(Best,y,func)))
    #print("final Temperature is: {}".format(t))
    return Quality(Best,y,func)




