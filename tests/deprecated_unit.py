import unittest
import doctest
import os

def load_tests(loader, tests, ignore):
    fullpath = 'MDAF/TestFunctions'
    testlist = []
    for func in os.scandir(fullpath):
        name = str(func.name)
        if(name.find('.py') and name.find('.old') == -1 and func.is_file()):
            spec = importlib.util.spec_from_file_location(name, fullpath)
            funcmodule = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(funcmodule)

            tests.addTests(doctest.DocTestSuite(funcmodule))
    return tests

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(load_tests())




import unittest
import os


from MDAF.TestFunctions import *
import doctest


#target = __import__("MDAF.py")

# Testing the test function representation workflow
def load_tests(loader, tests, ignore):

    fullpath = 'MDAF/TestFunctions'
    testlist = []
    for func in os.scandir(fullpath):
        name = str(func.name)
        if(name.find('.py') and name.find('.old') == -1 and func.is_file()):
            curtest = doctest.DocTestSuite(os.path.relpath('../'+func.path[:-3]+'.main.__module__'))
            testlist.append(curtest)
    tests.addTests(testlist)

    tests.addTests(doctest.DocTestSuite(Ackley2.main.__module__))
    for t in tests: return t

# run the suite
suite = load_tests(loader, tests, ignore)
runner = unittest.TextTestRunner()
runner.run(suite)