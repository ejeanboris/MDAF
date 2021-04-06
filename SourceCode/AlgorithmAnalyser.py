# directly running the DOE because existing surrogates can be explored with another workflow

import importlib.util
import multiprocessing
import time

from numpy import random as r



heuristicpath = "/home/remi/Documents/MDAF-GitLAB/SourceCode/SampleAlgorithms/SimmulatedAnnealing.py"
heuristic_name = "SimmulatedAnnealing"
testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin2.py", "/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin4.py", "/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Brown.py"]
funcnames = ["Bukin2", "Bukin4", "Brown"]
# testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin4.py"]
# funcnames = ["Bukin4"]

objs = 0
args = {"high": 200, "low": -200, "t": 1000, "p": 0.95}
scale = 2.5

def measure(heuristicpath, heuristic_name, funcpath, funcname, objs, args, scale, connection):
    # Seeding the random module for generating the initial point of the optimizer: Utilising random starting point for experimental validity
    r.seed(int(time.time()))

    # loading the heuristic object into the namespace and memory
    spec = importlib.util.spec_from_file_location(heuristic_name, heuristicpath)
    heuristic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(heuristic)

    testspec = importlib.util.spec_from_file_location(funcname, funcpath)
    func = importlib.util.module_from_spec(testspec)
    testspec.loader.exec_module(func)

    # Defining a random initial point to start testing the algorithms
    initpoint = [r.random() * scale, r.random() * scale]

    #This timer calculates directly the CPU time of the process (Nanoseconds)
    tic = time.process_time_ns()
    # running the test by calling the heuritic script with the test function as argument
    best = heuristic.main(func, objs, initpoint, args)
    toc = time.process_time_ns()
    # ^^ The timer ends right above this; the CPU time is then calculated below by simple difference ^^

    # Building the response
    response = "The optimum point obtained is: " + str(best) + "\nThe CPU time of the process was: " + str((toc - tic)*(10**-9))

    connection.send(response)



def doe(heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale):


    # logic variables to deal with the processes
    proc = []
    connections = {}

    # loading the test functions into the namespace and memory
    for idx, funcpath in enumerate(testfunctionpaths):
        funcname = funcnames[idx]
        # Creating the connection objects for communication between the heuristic and this module
        connections[funcname] = multiprocessing.Pipe(duplex=False)
        proc.append(multiprocessing.Process(target=measure, name=funcname, args=(heuristicpath, heuristic_name, funcpath, funcname, objs, args, scale, connections[funcname][1])))

    # defining the response variables
    responses = {}
    failedfunctions = {}
    processtiming = {}

    # defining some logic variables

    for idx,process in enumerate(proc):
        process.start()

    # Waiting for all the runs to be
    # multiprocessing.connection.wait([process.sentinel for process in proc])
    for process in proc: process.join()

    for process in proc:
        run = process.name
        if process.exitcode == 0: responses[run] = connections[run][0].recv()
        else:
            responses[run] = "this run was not successful"
            failedfunctions[run] = process.exitcode
        connections[run][0].close()
        connections[run][1].close()

    # display output
    print("\n\n||||| Responses |||||")
    for process in proc: print(process.name + "____\n" + str(responses[process.name]) + "\n_________________")


doe (heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale)