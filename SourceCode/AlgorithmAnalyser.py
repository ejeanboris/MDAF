# directly running the DOE because existing surrogates can be explored with another workflow

from numpy import random as r
import time
import importlib.util
import multiprocessing



# initialise the logic helpers
r.seed(int(time.time()))

heuristicpath = "/home/remi/Documents/MDAF-GitLAB/SourceCode/SampleAlgorithms/SimmulatedAnnealing.py"
heuristic_name = "SimmulatedAnnealing"
testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin2.py", "/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin4.py", "/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Brown.py"]
funcnames = ["Bukin2", "Bukin4", "Brown"]
# testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Brown.py"]
# funcnames = ["Brown"]

objs = 0
args = {"high": 200, "low": -200, "t": 1000, "p": 0.95}
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
        connections.append(multiprocessing.Pipe(duplex=False))
        proc.append(multiprocessing.Process(target=heuristic.main, name=funcnames[idx], args=(func, objs, initpoint, args, connections[idx][1])))


    responses = []
    failedfunctions = []
    processtiming = []

    for idx,process in enumerate(proc):
        # processtiming.append(time.tic())
        process.start()
        # connections[idx][1].close()

    # Waiting for all the runs to be done
    for process in proc: process.join()

    for idx,conn in enumerate(connections):
        if proc[idx].exitcode == 0: responses.append(conn[0].recv())
        else:
            responses.append("this run was mot successful")
            failedfunctions.append((funcnames[idx], proc[idx].exitcode))
        conn[0].close()
        conn[1].close()

    # display output
    print("\n\n||||| Responses |||||")
    for idx,response in enumerate(responses): print(funcnames[idx] + "____\n" + "started :" + str(initpoint) + "\nEnded  :" + str(responses[idx]) + "\n_________________")


doe (heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale)