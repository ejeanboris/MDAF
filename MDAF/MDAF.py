# directly running the DOE because existing surrogates can be explored with another workflow
from os import path
from os import sys
import importlib.util
import  multiprocessing
import time
import re
from numpy import random as rand
from numpy import array, isnan, NaN, asarray
import statistics
from functools import partial
import shutil

# Surrogate modelling

# Test function representation
from rpy2 import robjects as robjs
from rpy2.robjects.packages import importr
from rpy2 import rinterface

# Test function characteristics
import statistics as st


def installFalcoo(mirror = 'https://utstat.toronto.edu/cran/'):
    utils = importr('utils')
    utils.install_packages('flacco', repos=mirror)
    utils.install_packages('list', repos=mirror)

class counter:
    #wraps a function, to keep a running count of how many
    #times it's been called
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

def simulate(algName, algPath, funcname, funcpath, args, initpoint):
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
        quality = heuristic.main(testfunc, initpoint, args)
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

def measure(heuristicpath, funcpath, args, connection):
    '''
    This function runs a set of optimization flows for each test function. it returns the mean and standard deviation of the performance results
    '''
    
    #defining the heuristic's name
    heuristic_name = path.splitext(path.basename(heuristicpath))[0]

    #defining the test function's name
    funcname = path.splitext(path.basename(funcpath))[0]

    # Seeding the random module for generating the initial point of the optimizer: Utilising random starting point for experimental validity
    rand.seed(int(time.time()))

    # guetting the representation of the function
    funcChars = representfunc(funcpath)

    n = funcChars['dimmensions']
    upper = funcChars['upper']
    lower = funcChars['lower']

    if upper is not list: upper = [upper for i in range(n)]
    if lower is not list: lower = [lower for i in range(n)]


    scale = list()
    for i in range(n): 
        scale.append(upper[i] - lower[i])


    # Defining random initial points to start testing the algorithms
    initpoints = [[rand.random() * scale[i] + lower[i] for i in range(n)] for run in range(30)] #update the inner as [rand.random() * scale for i in range(testfuncDimmensions)]
    # building the iterable arguments
    partfunc = partial(simulate, heuristic_name, heuristicpath, funcname, funcpath, args)
    
    n_proc = multiprocessing.cpu_count() # Guetting the number of cpus
    with multiprocessing.Pool(processes = n_proc) as pool:
        # running the simulations
        newRun = pool.map(partfunc,initpoints)
        
    cpuTime = array([resl[0] for resl in newRun])
    quality = array([resl[1] for resl in newRun])
    numCalls = array([resl[2] for resl in newRun])
    converged = array([resl[3] for resl in newRun])

    cpuTime = cpuTime[~(isnan(cpuTime))]
    quality = quality[~(isnan(quality))]
    numCalls = numCalls[~(isnan(numCalls))]
    converged = converged[~(isnan(converged))]
    
    results = dict()
    results['cpuTime'] = array([statistics.fmean(cpuTime), statistics.stdev(cpuTime)])
    results['quality'] = array([statistics.fmean(quality), statistics.stdev(quality)])
    results['numCalls'] = array([statistics.fmean(numCalls), statistics.stdev(numCalls)])
    results['convRate'] = array([statistics.fmean(converged), statistics.stdev(converged)])

    connection.send((results,newRun))

def writerepresentation(funcpath, charas):
    # Save a backup copy of the function file
    shutil.copyfile(funcpath, funcpath + '.old')

    # create a string format of the representation variables
    representation = ''
    for line in list(charas):
        representation += '\n\t#_# ' + line + ': ' + repr(charas[line]).replace('\n','')
    representation+='\n\n\t#_# Represented: 1\n\n'

    # Creating the new docstring to be inserted into the file
    with open(funcpath, "r") as file:
        content = file.read()
        docstrs = re.findall(r"def main\(.*?\):.*?'''(.*?)'''.*?return\s+.*?", content, re.DOTALL)[0]
        docstrs += representation
        repl = "\\1"+docstrs+"\t\\2"

        # Create the new content of the file to replace the old. Replacing the whole thing
        pattrn = re.compile(r"(def main\(.*?\):.*?''').*?('''.*?return\s+.*?\n|$)", flags=re.DOTALL)
        newContent = pattrn.sub(repl, content, count=1)
    # Overwrite the test function file
    with open(funcpath,"w") as file:
        file.write(newContent)

def representfunc(funcpath, forced = False):
    if (funcpath.find('@') == 0): funcpath = path.dirname(__file__) + '/TestFunctions/' + funcpath[1:]

    #defining the function name
    funcname = path.splitext(path.basename(funcpath))[0]
    # loading the function to be represented
    spec = importlib.util.spec_from_file_location(funcname, funcpath)
    funcmodule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(funcmodule)

    # Finding the function characteristics inside the docstring
    if funcmodule.main.__doc__:
        regex = re.compile(r"#_#\s?(\w+):(.+)?\n") # this regular expression matches the characteristics already specified in the docstring section of the function  -- old exp: "#_#\s?(\w+):\s?([-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)"
        characs = re.findall(regex, funcmodule.main.__doc__)
        results = {}
        for charac in characs:
            results[charac[0]] = eval(charac[1])

        # Automatically generate the representation if the docstrings did not return anything
        if not ('Represented' in results):
            print("Warning, the Representation of the Test Function has not been specified\n===\n******Calculating the Characteristics******")
            n = int(results['dimmensions'])
            blocks = int(1+10/n)
            if blocks< 3: blocks=3

            # Importing FLACCO using rpy2
            flacco = importr('flacco')
            
            # creating the r functions
            rlist = robjs.r['list']
            rapply = robjs.r['apply']
            rvector = robjs.r['c']
            r_unlist = robjs.r['unlist']
            rtestfunc = rinterface.rternalize(funcmodule.main)

            # Verify if a list of limits has been specified for all dimensions or if all dimensions will use the same boundaries
            if (type(results['lower']) is list): 
                lowerval = r_unlist(rvector(results['lower']))
                upperval = r_unlist(rvector(results['upper']))
            else:
                lowerval = results['lower']
                upperval = results['upper']

            X = flacco.createInitialSample(n_obs = 500, dim = n, control = rlist(**{'init_sample.type' : 'lhs', 'init_sample.lower' : lowerval, 'init_sample.upper' : upperval}))
            y = rapply(X, 1, rtestfunc)
            testfuncobj = flacco.createFeatureObject(**{'X': X, 'y': y, 'fun': rtestfunc, 'lower': lowerval, 'upper': upperval, 'blocks': blocks, 'force': forced})
            
            # these are the retained features. Note that some features are being excluded for being problematic and to avoid overcomplicating the neural network.... the feature sets are redundant and the most relevant ones have been retained
            # the excluded feature sets are: 'bt', 'ela_level'
            # feature sets that require special attention: 'cm_angle', 'cm_grad', 'limo', 'gcm' (large set with some nans), 
            featureset = ['cm_angle','cm_conv','cm_grad','ela_conv','ela_curv','ela_distr','ela_local','ela_meta','basic','disp','limo','nbc','pca','gcm','ic']
            pyfeats = dict()
            for feature in featureset:
                rawfeats = flacco.calculateFeatureSet(testfuncobj, set=feature)
                pyfeats[feature] = asarray(rawfeats)
            
            writerepresentation(funcpath, pyfeats)

    return results



def doe(heuristicpath, testfunctionpaths, args):
    for i,path in enumerate(testfunctionpaths): if (path.find('@') == 0): testfunctionpaths[i] = path.dirname(__file__) + '/TestFunctions/' + testfunctionpaths[1:]
    if (heuristicpath.find('@') == 0): heuristicpath = path.dirname(__file__) + '/TestFunctions/' + heuristicpath[1:]

    #defining the function's name
    funcnames = [path.splitext(path.basename(funcpath))[0] for funcpath in testfunctionpaths]

    #defining the heuristic's name
    #heuristic_name = path.splitext(path.basename(heuristicpath))[0]

    # logic variables to deal with the processes
    proc = []
    connections = {}

    # loading the test functions into the namespace and memory
    for idx, funcpath in enumerate(testfunctionpaths):
        funcname = funcnames[idx]
        # Creating the connection objects for communication between the heuristic and this module
        connections[funcname] = multiprocessing.Pipe(duplex=False)
        proc.append(multiprocessing.Process(target=measure, name=funcname, args=(heuristicpath, funcpath, args, connections[funcname][1])))

    # defining the response variables
    responses = {}
    failedfunctions = {}

    # Starting the subprocesses for each testfunction
    for idx,process in enumerate(proc):
        process.start()

    # Waiting for all the runs to be done
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
    
    #return the performance values
    return responses


# %%
