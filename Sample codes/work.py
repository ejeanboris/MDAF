if __name__ == '__main__':
    heuristicpath = "SampleAlgorithms/SimmulatedAnnealing.py"
    heuristic_name = "SimmulatedAnnealing"
    #testfunctionpaths = ["TestFunctions/Bukin2.py", "TestFunctions/Bukin4.py", "TestFunctions/Brown.py"]
    funcnames = ["Bukin2", "Bukin4", "Brown"]
    testfunctionpaths = ["/home/remi/Documents/MDAF-GitLAB/SourceCode/TestFunctions/Brown.py"]
    # funcnames = ["Bukin4"]
    
    args = {"t": 1000, "p": 0.95, "objs": 0}
        
    #data = doe (heuristicpath, testfunctionpaths, args)
    #print(data['Brown'])
    representfunc("TestFunctions/Brown.py", forced = True)
    
    


from MDAF import *

testfunctionpaths = ["@Bukin2.py","@Bukin4.py","@Brown.py"]
heuristicpath = "@SimmulatedAnnealing.py"
args = {"t": 1000, "p": 0.95, "objs": 0}
data = doe (heuristicpath, testfunctionpaths, args)
print(data)
