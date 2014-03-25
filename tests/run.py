# -*- coding: utf-8 -*-

import os
import sys

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)

from unittest import main, TestSuite, findTestCases, TextTestRunner

def get_test_module_names():
    file_names = os.listdir(os.curdir)
    for fn in file_names:
        if fn.startswith('test') and fn.endswith('.py'):
            yield 'tests.' + fn[:-3]

def suite():
    alltests = TestSuite()

    for module_name in get_test_module_names():
        module = __import__(module_name, fromlist=[module_name])
        alltests.addTest(findTestCases(module))

    return alltests

try:
    from test_config import LOG_NAME
except ImportError:
    LOG_NAME = 'test.log'

if __name__ == '__main__':

    try:
        from test_config import LOG_NAME
    except ImportError:
        LOG_NAME = 'test.log'    

    log_fd = open(LOG_NAME, 'w')
    test_runner = TextTestRunner(stream=log_fd)
    main(defaultTest='suite', testRunner=test_runner)
