'''
 * A stack unit test.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

import unittest
import sys
import os

if __package__:
    from .linked_stack import LinkedStack
    from .abstract_stack import EmptyStack
else:
    sys.path.append(os.path.dirname(__file__))
    from linked_stack import LinkedStack
    from abstract_stack import EmptyStack


class LinkedStackTest(unittest.TestCase):

    def setUp(self):
        self.stack = LinkedStack()
    
    
    def test_empty_stack(self):
        self.assertTrue(self.stack.empty())
        self.assertEqual(len(self.stack), 0)
    
    
    def test_pop_of_empty(self):
        with self.assertRaises(EmptyStack):
            self.stack.pop()
        
    
    def test_peek_of_empty(self):
        with self.assertRaises(EmptyStack):
            self.stack.peek()
            
    
    def test_push(self):
        self.stack.push(3)
        self.assertEqual(len(self.stack), 1)
    
    
    def test_pop(self):
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(len(self.stack), 0)
    
    
    def test_peek(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(len(self.stack), 1)
    
    
    def test_general(self):
        self.assertTrue(self.stack.empty())
        self.stack.push(5)
        self.assertFalse(self.stack.empty())
        self.stack.push(6)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.peek(), 6)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 6)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.peek(), 5)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(len(self.stack), 0)
        self.assertTrue(self.stack.empty())
    
    
    def test_iteration(self):
        with self.assertRaises(StopIteration):
            iter_obj = iter(self.stack)
            next(iter_obj)
            
        self.stack.push(6)
        self.stack.push(7)
        self.stack.push(8)
        self.assertEqual(len(self.stack), 3)
        
        iter_obj = iter(self.stack)
        self.assertEqual(next(iter_obj), 6)
        self.assertEqual(next(iter_obj), 7)
        self.assertEqual(next(iter_obj), 8)
        with self.assertRaises(StopIteration):
            next(iter_obj)
    
    
    def test_to_string(self):
        self.assertEqual(str(self.stack), "[]")
        self.stack.push('a')
        self.assertEqual(str(self.stack), "[a]")
        self.stack.push('b')
        self.assertEqual(str(self.stack), "[a, b]")
        self.stack.push('c')
        self.stack.push('d')
        self.stack.push('e')
        self.stack.push('f')
        self.assertEqual(str(self.stack), "[a, b, c, d, e, f]")
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(str(self.stack), "[a, b, c, d]")


if __name__ == '__main__':
    unittest.main()