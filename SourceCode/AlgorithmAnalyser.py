# directly running the DOE because existing surrogates can be explored with another workflow

from numpy import random as r
import time
import importlib.util
import multiprocessing


# initialise the logic helpers
r.seed(int(time.time()))

heuristicpath = "/home/remi/Documents/MDAF-GitLAB/SourceCode/SampleAlgorithms/SimmulatedAnnealing.py"
heuristic_name = "SimmulatedAnnealing"
testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin2.py", "/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin4.py", "/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin6.py"]
funcnames = ["Bukin2", "Bukin4", "Bukin6"]
objs = 0
args = {"high": 200, "low": -200, "t": 100, "p": 0.95}
scale = 2.5


def doe(heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale):
    spec = importlib.util.spec_from_file_location(heuristic_name, heuristicpath)
    heuristic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(heuristic)
    proc = list()
    connections = []
    #heuristic.MyClass()
    for idx, funcpath in enumerate(testfunctionpaths):
        testspec = importlib.util.spec_from_file_location(funcnames[idx], funcpath)
        func = importlib.util.module_from_spec(testspec)
        testspec.loader.exec_module(func)
        #func.MyClass()
        initpoint = [r.random() * scale, r.random() * scale]
        connections.append(multiprocessing.Pipe())
        proc.append(multiprocessing.Process(target=heuristic.main, name=funcnames[idx], args=(func, objs, initpoint, args, connections[idx][0])))
    responses = []
    for idx,process in enumerate(proc):
        process.start()
        responses.append(connections[idx][1].recv())

    print("started :" + str(initpoint) + "\nEnded  :" + str(responses[0]))


doe (heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale)