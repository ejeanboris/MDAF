import unittest
import os

from MDAF.MDAF import representfunc
from MDAF.MDAF import doe

#target = __import__("MDAF.py")

# Testing the test function representation workflow
class Test_representfunc(unittest.TestCase):
    def testexternalfuncs(self):
        """
        Test that the function can calculate the representation and write to the function docstring
        """
        funcpath = 'tests/Bukin2.py'
        #funcpath_backup = 'tests/Bukin2.py.old'

        results = representfunc(funcpath, forced = True)

        with open(funcpath,"r") as file:
            content = file.read()
            reprCheck = bool(content.find('#_# Represented: 1'))

        #os.remove(funcpath) 
        #os.replace(funcpath_backup, funcpath)
        self.assertTrue(reprCheck)
        self.assertIsInstance(results, dict)
    
    def testinternalfuncs(self):
        """
        Test that the function can calculate the representation and write to the function docstring
        """
        funcpath = '@Bukin2.py'
        funcverify = 'MDAF/TestFunctions/Bukin2.py'
        #funcpath_backup = 'tests/Bukin2.py.old'

        results = representfunc(funcpath, forced = True)

        with open(funcverify,"r") as file:
            content = file.read()
            reprCheck = bool(content.find('#_# Represented: 1'))

        #os.remove(funcpath) 
        #os.replace(funcpath_backup, funcpath)
        self.assertTrue(reprCheck)
        self.assertIsInstance(results, dict)



# Testing the flacco installation workflow
class Test_flaccoInstall(unittest.TestCase):
    def testoutput(self):
        """
        Test that the flacco packages are able to install automatically
        """
        #installFalcoo()


# Testing the DOE execution workflow
class Test_DOE(unittest.TestCase):
    def testexternalfuncs(self):
        """
        Test that it can execute a DOE and output the dictionarry of the results
        """
        testfunctionpaths = ["tests/Bukin2.py"]
        heuristicpath = "tests/SimmulatedAnnealing.py"
        args = {"t": 1000, "p": 0.95, "objs": 0}
        data = doe (heuristicpath, testfunctionpaths, args)
        self.assertIsInstance(data, dict)
    
    def testinternalfuncs(self):
        """
        Test that it can execute a DOE and output the dictionarry of the results
        """
        testfunctionpaths = ["@Bukin2.py"]
        heuristicpath = "@SimmulatedAnnealing.py"
        args = {"t": 1000, "p": 0.95, "objs": 0}
        data = doe (heuristicpath, testfunctionpaths, args)
        print(data)
        self.assertIsInstance(data, dict)


# Testing the surrogate modelling workflow
class Test_surrogate(unittest.TestCase):
    def testoutput(self):
        """
        Test that it can generate a neural network approximation of the algorithm's performance expectation
        """
        #tbd



if __name__ == '__main__':
    unittest.main()