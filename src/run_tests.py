'''
 * A file to run all the unit tests of the project.
 *
 * @author Cosimo Giovanni Negri
 * @date   29 Aug 2022
'''

import unittest

from datastructures.linkedlist.test_doubly_linked_list import DoublyLinkedListTest
from datastructures.queue.test_queue import QueueTest
from datastructures.stack.test_stack import StackTest
from datastructures.hashtable.test_hash_table import HashTableTest
from datastructures.set.test_set import SetTest

# add automatic imports with a recursive os.walk ???

# for each file that starts with "test_", look for something
# that ends with "Test" in dir(file)


def get_tests(unit_test):
    '''
    Return a list containing all the TestCase methods
    in the given unit test.
    '''
    tests = []
    for element_name in dir(unit_test):
        if element_name.startswith('test_'):
            tests.append(unit_test(element_name))
            
    return tests


def print_message(unit_test_name, tests_num):
    '''
    Print a message containing the number of TestCase methods
    in the given unit test.
    '''
    print("{:<25}|   {:<2} tests   |".format(unit_test_name, tests_num))


def expand_suite(suite, unit_test, print=True):
    '''
    Expand the given suite with all the TestCase methods
    in the given unit test.
    NOTE: print a message containing some informations
    unless the third argument is set to False.
    '''
    tests = get_tests(unit_test)
    tests_num = len(tests)
    unit_test_name = unit_test.__name__
    
    if print:
        print_message(unit_test_name, tests_num)
    
    suite.addTests(tests)


if __name__ == '__main__':
    # Initialize some variables
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    
    # Expand the suite with all the tests and print some data
    expand_suite(suite, DoublyLinkedListTest)
    expand_suite(suite, QueueTest)
    expand_suite(suite, StackTest)
    expand_suite(suite, HashTableTest)
    expand_suite(suite, SetTest)
    
    # Run all the tests
    runner.run(suite)