'''
 * A queue unit test.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

import unittest
import sys
import os

if __package__:
    from .linked_queue import LinkedQueue
else:
    sys.path.append(os.path.dirname(__file__))
    from linked_queue import LinkedQueue


class LinkedQueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = LinkedQueue()
    
    
    def test_empty_queue(self):
        self.assertTrue(self.queue.isempty())
        self.assertEqual(len(self.queue), 0)
    
    
    def test_dequeue_of_empty(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        
    
    def test_peek_of_empty(self):
        with self.assertRaises(IndexError):
            self.queue.peek()
            
    
    def test_enqueue(self):
        self.queue.enqueue(3)
        self.assertEqual(len(self.queue), 1)
    
    
    def test_dequeue(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(len(self.queue), 0)
    
    
    def test_peek(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 3)
        self.assertEqual(len(self.queue), 1)
    
    
    def test_general(self):
        self.assertTrue(self.queue.isempty())
        self.queue.enqueue(5)
        self.assertFalse(self.queue.isempty())
        self.queue.enqueue(6)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.peek(), 5)
        self.assertEqual(len(self.queue), 2)
        self.assertEqual(self.queue.dequeue(), 5)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.peek(), 6)
        self.assertEqual(len(self.queue), 1)
        self.assertEqual(self.queue.dequeue(), 6)
        self.assertEqual(len(self.queue), 0)
        self.assertTrue(self.queue.isempty())
    
    
    def test_iteration(self):
        with self.assertRaises(StopIteration):
            iter_obj = iter(self.queue)
            next(iter_obj)
            
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        self.queue.enqueue(8)
        self.assertEqual(len(self.queue), 3)
        
        iter_obj = iter(self.queue)
        self.assertEqual(next(iter_obj), 6)
        self.assertEqual(next(iter_obj), 7)
        self.assertEqual(next(iter_obj), 8)
        with self.assertRaises(StopIteration):
            next(iter_obj)
    
    
    def test_to_string(self):
        self.assertEqual(str(self.queue), "[]")
        self.queue.enqueue('a')
        self.assertEqual(str(self.queue), "[a]")
        self.queue.enqueue('b')
        self.assertEqual(str(self.queue), "[a, b]")
        self.queue.enqueue('c')
        self.queue.enqueue('d')
        self.queue.enqueue('e')
        self.queue.enqueue('f')
        self.assertEqual(str(self.queue), "[a, b, c, d, e, f]")
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(str(self.queue), "[c, d, e, f]")


if __name__ == '__main__':
    unittest.main()