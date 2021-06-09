import unittest
import os
import importlib.util as utl

from MDAF.TestFunctions import *
import doctest


# Testing the test function representation workflow
def load_tests(loader, tests, ignore):
    fullpath = 'MDAF/TestFunctions'
    for func in os.scandir(fullpath):
        name = str(func.name)
        if(name.find('.py') and name.find('.old') == -1 and func.is_file() and name.find('__init__.py')==-1):
            spec = utl.spec_from_file_location(name[-3], fullpath+'/'+name)
            funcmodule = utl.module_from_spec(spec)
            spec.loader.exec_module(funcmodule)

            tests.addTests(doctest.DocTestSuite(funcmodule))
    return tests

