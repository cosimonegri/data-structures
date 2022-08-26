'''
 * A queue unit test.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *                         liujingkun, liujkon@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   26 Aug 2022
'''

from LinkedQueue import LinkedQueue
from Queue import EmptyQueue
import unittest


class LinkedQueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = LinkedQueue()
    
    
    def testEmptyQueue(self):
        self.assertTrue(self.queue.isEmpty())
        self.assertEqual(len(self.queue), 0)
    
    
    def testDequeueOfEmpty(self):
        with self.assertRaises(EmptyQueue):
            self.queue.dequeue()
        
    
    def testPeekOfEmpty(self):
        with self.assertRaises(EmptyQueue):
            self.queue.peek()
            
    
    def testEnqueue(self):
        self.queue.enqueue(3)
        self.assertEqual(len(self.queue), 1)
    
    
    def testDequeue(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(len(self.queue), 0)
    
    
    def testPeek(self):
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 3)
        self.assertEqual(len(self.queue), 1)
    
    
    def testGeneral(self):
        self.assertTrue(self.queue.isEmpty())
        self.queue.enqueue(5)
        self.assertFalse(self.queue.isEmpty())
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
        self.assertTrue(self.queue.isEmpty())
    
    
    def testIteration(self):
        with self.assertRaises(StopIteration):
            iterObj = iter(self.queue)
            next(iterObj)
            
        self.queue.enqueue(6)
        self.queue.enqueue(7)
        self.queue.enqueue(8)
        self.assertEqual(len(self.queue), 3)
        
        iterObj = iter(self.queue)
        self.assertEqual(next(iterObj), 6)
        self.assertEqual(next(iterObj), 7)
        self.assertEqual(next(iterObj), 8)
        with self.assertRaises(StopIteration):
            next(iterObj)
    
    
    def testToString(self):
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