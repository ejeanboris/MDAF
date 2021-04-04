# directly running the DOE because existing surrogates can be explored with another workflow

from numpy import random as r
import time
import importlib.util
import multiprocessing


# initialise the logic helpers
r.seed(int(time.time()))

heuristicpath = "/home/remi/Documents/MDAF-GitLAB/SourceCode/SampleAlgorithms/SimmulatedAnnealing.py"
heuristic_name = "SimmulatedAnnealing"
testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin2.py"]
funcnames = ["Bukin2"]
objs = 0
args = {"high": 200, "low": -200, "t": 0.01, "p": 0.8}
scale = 62


def doe(heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale):
    spec = importlib.util.spec_from_file_location(heuristic_name, heuristicpath)
    heuristic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(heuristic)
    proc = list()
    #heuristic.MyClass()
    for idx, funcpath in enumerate(testfunctionpaths):
        testspec = importlib.util.spec_from_file_location(funcnames[idx], funcpath)
        func = importlib.util.module_from_spec(testspec)
        testspec.loader.exec_module(func)
        #func.MyClass()
        initpoint = [r.random() * scale, r.random() * scale]
        proc.append(multiprocessing.Process(target=heuristic.main, name=funcnames[idx], args=(func, objs, initpoint, args)))
        best = proc[idx].run()
        print("started :" + str(initpoint) + "\nEnded  :" + str(best))

# simulatedAnnealing(S = [9.00,4.00],y = 0,high = 10,low = -8,t =0.01,p = 0.8)
# proc = subprocess.call(["python", heuristic, "arg-15", "arg2", "argN"])

doe (heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale)