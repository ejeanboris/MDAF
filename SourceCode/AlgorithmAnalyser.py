# directly running the DOE because existing surrogates can be explored with another workflow
from os import path
from os import sys
import importlib.util
import  multiprocessing
import time
import re
from numpy import random as r
from numpy import *
import statistics
from functools import partial
import shutil

# Surrogate modelling
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Test function representation
from rpy2 import robjects as robjs
from rpy2.robjects.packages import importr
from rpy2 import rinterface

# Test function characteristics
import statistics as st
from scipy import signal, misc, ndimage


class counter:
    #wraps a function, to keep a running count of how many
    #times it's been called
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

def simulate(algName, algPath, funcname, funcpath, objs, args, initpoint):
    # loading the heuristic object into the namespace and memory
    spec = importlib.util.spec_from_file_location(algName, algPath)
    heuristic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(heuristic)

    # loading the test function object into the namespace and memory
    testspec = importlib.util.spec_from_file_location(funcname, funcpath)
    func = importlib.util.module_from_spec(testspec)
    testspec.loader.exec_module(func)

    # defining a countable test function
    @counter
    def testfunc(args):
        return func.main(args)

    # using a try statement to handle potential exceptions raised by child processes like the algorithm or test functions or the pooling algorithm
    try:
        #This timer calculates directly the CPU time of the process (Nanoseconds)
        tic = time.process_time_ns()
        # running the test by calling the heuritic script with the test function as argument
        quality = heuristic.main(testfunc, objs, initpoint, args)
        toc = time.process_time_ns()
        # ^^ The timer ends right above this; the CPU time is then calculated below by simple difference ^^

        # CPU time in seconds
        cpuTime = (toc - tic)*(10**-9)
        numCalls = testfunc.count
        converged = 1
    except:
        quality = NaN
        cpuTime = NaN
        numCalls = testfunc.count
        converged = 0
    return cpuTime, quality, numCalls, converged

def measure(heuristicpath, heuristic_name, funcpath, funcname, objs, args, scale, connection):
    '''
    This function runs each optimization process of the heuristic with one test function
    '''
    
    # Seeding the random module for generating the initial point of the optimizer: Utilising random starting point for experimental validity
    r.seed(int(time.time()))


    # Defining random initial points to start testing the algorithms
    initpoints = [[r.random() * scale, r.random() * scale] for run in range(30)] #update the inner as [r.random() * scale for i in range(testfuncDimmensions)]
    # building the iterable arguments
    partfunc = partial(simulate, heuristic_name, heuristicpath, funcname, funcpath, objs, args)

    with multiprocessing.Pool(processes = 3) as pool:
        # running the simulations
        newRun = pool.map(partfunc,initpoints)
        
    cpuTime = [resl[0] for resl in newRun]
    quality = [resl[1] for resl in newRun]
    numCalls = [resl[2] for resl in newRun]
    converged = [resl[3] for resl in newRun]
    
    results = dict()
    results['cpuTime'] = array([statistics.mean(cpuTime), statistics.stdev(cpuTime)])
    results['quality'] = array([statistics.mean(quality), statistics.stdev(quality)])
    results['numCalls'] = array([statistics.mean(numCalls), statistics.stdev(numCalls)])
    results['convRate'] = array([statistics.mean(converged), statistics.stdev(converged)])

    connection.send((results,newRun))

def writerepresentation(funcpath, charas):
    # Save a backup copy of the function file
    shutil.copyfile(funcpath, funcpath + '.old')

    # create a string format of the representation variables
    representation = ''
    for line in list(charas):
        representation += '\n\t#_# ' + line + ': ' + str(charas[line])
    representation+='\n'

    # Creating the new docstring to be inserted into the file
    with open(funcpath, "r") as file:
        content = file.read()
        docstrs = re.findall("def main\(.*?\):.*?'''(.*?)'''.*?return\s+.*?", content, re.DOTALL)[0]
        docstrs += representation
        repl = "\\1"+docstrs+"\t\\2"

        # Create the new content of the file to replace the old. Overwriting the whole thing
        pattrn = re.compile("(def main\(.*?\):.*?''').*?('''.*?return\s+.*?\n|$)", flags=re.DOTALL)
        newContent = pattrn.sub(repl, content, count=1)
    # Overwrite the test function file
    with open(funcpath,"w") as file:
        file.write(newContent)

def representfunc(funcpath):
    #defining the function name
    funcname = path.splitext(path.basename(funcpath))[0]
    # loading the function to be represented
    spec = importlib.util.spec_from_file_location(funcname, funcpath)
    funcmodule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(funcmodule)

    # Finding the function characteristics inside the docstring
    if funcmodule.main.__doc__:
        regex = re.compile("#_#\s?(\w+):\s?([-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)")
        characs = re.findall(regex, funcmodule.main.__doc__)
        results = {}
        for charac in characs:
            results[charac[0]] = float(charac[1])

        # Automatically generate the representation if the docstrings did not return anything
        if not ('Represented' in results):
            print("Warning, the Representation of the Test Function has not been specified\n===\n******Calculating the Characteristics******")
            n = int(results['dimmensions'])
            
            execpath = sys.executable
            
            # creating the r functions
            rlist = robjs.r['list']
            rapply = robjs.r['apply']
            rtestfunc = rinterface.rternalize(funcmodule.main)

            ###
            lower =-10
            upper = 10
            X = flacco.createInitialSample(n_obs = 500, dim = 2, control = rlist(init_sample_type = 'lhs', init_sample_lower = lower, init_sample_upper = upper))
            y = rapply(X, 1, rtestfunc)
            testfuncobj = flacco.createFeatureObject(X = X, y = y, fun = rtestfunc, lower = lower, upper = upper, blocks = 10)
            
            rawfeats = flacco.calculateFeatureSet(testfuncobj, set='ela_meta')

            pyfeat = asarray(rawfeats)
            
            
            
            
            writerepresentation(funcpath, results)


    return results



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
    print("\n\n||||| Responses: [mean,stdDev] |||||")
    for process in proc: print(process.name + "____\n" + str(responses[process.name][0]) + "\n_________________")
    
    #return output
    return responses

if __name__ == '__main__':
    heuristicpath = "SampleAlgorithms/SimmulatedAnnealing.py"
    heuristic_name = "SimmulatedAnnealing"
    testfunctionpaths = ["TestFunctions/Bukin2.py", "TestFunctions/Bukin4.py", "TestFunctions/Brown.py"]
    funcnames = ["Bukin2", "Bukin4", "Brown"]
    # testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Bukin4.py"]
    # funcnames = ["Bukin4"]

    # Installing the packages needed for FLACCO
    utils = importr('utils')
    #utils.install_packages('flacco', repos='https://utstat.toronto.edu/cran/')
    #utils.install_packages('list', repos='https://utstat.toronto.edu/cran/')
    ####utils.install_packages('reticulate', repos='https://utstat.toronto.edu/cran/')

    reticulate = importr('reticulate')
    flacco = importr('flacco')

    objs = 0
    args = {"high": 200, "low": -200, "t": 1000, "p": 0.95}
    scale = 1
        
    # data = doe (heuristicpath, heuristic_name, testfunctionpaths, funcnames, objs, args, scale)
    # print([point[2] for point in data['Bukin2'][1]])
    representfunc("TestFunctions/Bukin2.py")


# %%
