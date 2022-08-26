'''
 * A doubly linked list unit test.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   25 Aug 2022
'''

from DoublyLinkedList import DoublyLinkedList, EmptyList, InvalidIndex
import unittest
from collections import deque
import random


class DoublyLinkedListTest(unittest.TestCase):
    
    def setUp(self):
        self.LOOPS = 300
        self.SIZE = 40
        self.NUM_NULLS = self.SIZE // 5
        self.MAX_RANDOM_NUM = 250
        
        self.list = DoublyLinkedList()
    
    
    def testEmptyList(self):
        self.assertTrue(self.list.isEmpty())
        self.assertEqual(len(self.list), 0)
    
    
    def testPopOfEmpty(self):
        with self.assertRaises(EmptyList):
            self.list.pop()
    
    
    def testPopLeftOfEmpty(self):
        with self.assertRaises(EmptyList):
            self.list.popLeft()
    
    
    def testPeekRightOfEmpty(self):
        with self.assertRaises(EmptyList):
            self.list.peekRight()
    
    
    def testPeekLeftOfEmpty(self):
        with self.assertRaises(EmptyList):
            self.list.peekLeft()
    
    
    def testAppend(self):
        self.list.append(3)
        self.assertEqual(len(self.list), 1)
        self.list.append(5)
        self.assertEqual(len(self.list), 2)
    
    
    def testAppendLeft(self):
        self.list.appendLeft(3)
        self.assertEqual(len(self.list), 1)
        self.list.appendLeft(5)
        self.assertEqual(len(self.list), 2)
    
    
    def testAddAt(self):
        with self.assertRaises(InvalidIndex):
            self.list.addAt(-1, 5)
        with self.assertRaises(InvalidIndex):
            self.list.addAt(1, 5)
        self.list.addAt(0, 1)
        self.assertEqual(len(self.list), 1)
        self.list.addAt(1, 2)
        self.assertEqual(len(self.list), 2)
        self.list.addAt(1, 3)
        self.assertEqual(len(self.list), 3)
        self.list.addAt(2, 4)
        self.assertEqual(len(self.list), 4)
        self.list.addAt(1, 8)
        self.assertEqual(len(self.list), 5)
    
    
    def testPop(self):
        self.list.append(5)
        self.assertEqual(self.list.pop(), 5)
        self.assertTrue(self.list.isEmpty())
        
    
    def testPopLeft(self):
        self.list.appendLeft(3)
        self.assertEqual(self.list.popLeft(), 3)
        self.assertTrue(self.list.isEmpty())
    
    
    def testRemoveAt(self):
        with self.assertRaises(InvalidIndex):
            self.list.removeAt(-1)
        with self.assertRaises(InvalidIndex):
            self.list.removeAt(0)
        with self.assertRaises(InvalidIndex):
            self.list.removeAt(1)
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(4)
        self.list.removeAt(0)
        self.list.removeAt(1)
        self.assertEqual(self.list.peekRight(), 4)
        self.assertEqual(self.list.peekLeft(), 2)
        self.list.removeAt(1)
        self.list.removeAt(0)
        self.assertEqual(len(self.list), 0)
    
    
    def testRemove(self):
        self.assertFalse(self.list.remove('a'))
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        self.list.append('d')
        self.list.append('e')
        self.list.append('f')
        self.list.append('a')
        self.assertTrue(self.list.remove('b'))
        self.assertTrue(self.list.remove('a'))
        self.assertTrue(self.list.remove('d'))
        self.assertTrue(self.list.remove('e'))
        self.assertTrue(self.list.remove('c'))
        self.assertTrue(self.list.remove('f'))
        self.assertTrue(self.list.remove('a'))
        self.assertEqual(len(self.list), 0)   
    
    
    def testPeekRight(self):
        self.list.append(5)
        self.assertEqual(self.list.peekRight(), 5)
        self.assertEqual(len(self.list), 1)
    
    
    def testPeekLeft(self):
        self.list.appendLeft(3)
        self.assertEqual(self.list.peekLeft(), 3)
        self.assertEqual(len(self.list), 1)
    
    
    def testPeek(self):
        # 5
        self.list.appendLeft(5)
        self.assertEqual(self.list.peekRight(), 5)
        self.assertEqual(self.list.peekLeft(), 5)
        
        # 6 - 5
        self.list.appendLeft(6)
        self.assertEqual(self.list.peekRight(), 5)
        self.assertEqual(self.list.peekLeft(), 6)
        
        # 7 - 6 - 5
        self.list.appendLeft(7)
        self.assertEqual(self.list.peekRight(), 5)
        self.assertEqual(self.list.peekLeft(), 7)
        
        # 7 - 6 - 5 - 8
        self.list.append(8)
        self.assertEqual(self.list.peekRight(), 8)
        self.assertEqual(self.list.peekLeft(), 7)
        
        # 7 - 6 - 5
        self.list.pop()
        self.assertEqual(self.list.peekRight(), 5)
        self.assertEqual(self.list.peekLeft(), 7)
        
        # 7 - 6
        self.list.pop()
        self.assertEqual(self.list.peekRight(), 6)
        self.assertEqual(self.list.peekLeft(), 7)
        
        # 6
        self.list.popLeft()
        self.assertEqual(self.list.peekRight(), 6)
        self.assertEqual(self.list.peekLeft(), 6)
    
    
    def testClear(self):
        self.list.append(22)
        self.list.append(33)
        self.list.append(44)
        self.assertEqual(len(self.list), 3)
        self.list.clear()
        self.assertEqual(len(self.list), 0)
        self.list.append(22)
        self.list.append(33)
        self.list.append(44)
        self.assertEqual(len(self.list), 3)
        self.list.clear()
        self.assertEqual(len(self.list), 0)
    
    
    def testIndex(self):
        self.assertEqual(self.list.index(3), None)
        self.list.append(22)
        self.assertEqual(self.list.index(22), 0)
        self.list.append(33)
        self.list.append(44)
        self.assertEqual(self.list.index(33), 1)
        self.assertEqual(self.list.index(44), 2)
        self.assertEqual(self.list.index(55), None)
        
    
    def testRandomRemove(self):
        pythonList = deque()
        
        for _ in range(self.LOOPS):
            randNums = self.getRandList()
            
            for value in randNums:
                self.list.append(value)
                pythonList.append(value)
            
            random.shuffle(randNums)
            
            for value in randNums:
                self.assertTrue(self.list.remove(value))
                self.assertEqual(pythonList.remove(value), None)
                
                self.assertEqual(len(self.list), len(pythonList))
                
                iter1 = iter(self.list)
                iter2 = iter(pythonList)
                
                while True:
                    try:
                        value1 = next(iter1)
                        value2 = next(iter2)
                    except StopIteration:
                        break
                    
                    self.assertEqual(value1, value2)
                
            self.assertEqual(len(self.list), 0)
            self.assertEqual(len(pythonList), 0)
    
    
    def testRandomRemoveAt(self):
        pythonList = deque()
        
        for _ in range(self.LOOPS):
            randNums = self.getRandList()
            
            for value in randNums:
                self.list.append(value)
                pythonList.append(value)
            
            for _ in range(len(randNums)):
                index = random.randint(0, len(self.list) - 1)
                
                value1 = self.list.removeAt(index)
                value2 = pythonList[index]
                del pythonList[index]
                
                self.assertEqual(value1, value2)
                self.assertEqual(len(self.list), len(pythonList))
                
                iter1 = iter(self.list)
                iter2 = iter(pythonList)
                
                while True:
                    try:
                        value1 = next(iter1)
                        value2 = next(iter2)
                    except StopIteration:
                        break
                    
                    self.assertEqual(value1, value2)
            
            self.assertEqual(len(self.list), 0)
            self.assertEqual(len(pythonList), 0)
    
    
    def testRandomIndex(self):
        pythonList = deque()
        
        for _ in range(self.LOOPS):
            self.list.clear()
            pythonList.clear()
            
            randNums = self.getUniqueRandList()
            
            for value in randNums:
                self.list.append(value)
                pythonList.append(value)
            
            random.shuffle(randNums)
            
            for value in randNums:
                index1 = self.list.index(value)
                index2 = pythonList.index(value)
                
                self.assertEqual(index1, index2)
                self.assertEqual(len(self.list), len(pythonList))
                
                iter1 = iter(self.list)
                iter2 = iter(pythonList)
                
                while True:
                    try:
                        value1 = next(iter1)
                        value2 = next(iter2)
                    except StopIteration:
                        break
                    
                    self.assertEqual(value1, value2)
            
            self.assertEqual(len(self.list), len(randNums))
            self.assertEqual(len(pythonList), len(randNums))
    
    
    def testContains(self):
        self.assertFalse(3 in self.list)
        self.list.append(3)
        self.assertTrue(3 in self.list)
        self.assertEqual(len(self.list), 1)
    
    
    def testIteration(self):
        with self.assertRaises(StopIteration):
            iterObj = iter(self.list)
            next(iterObj)
            
        self.list.append(6)
        self.list.append(7)
        self.list.append(8)
        self.assertEqual(len(self.list), 3)
        
        iterObj = iter(self.list)
        self.assertEqual(next(iterObj), 6)
        self.assertEqual(next(iterObj), 7)
        self.assertEqual(next(iterObj), 8)
        with self.assertRaises(StopIteration):
            next(iterObj)
    
    
    def testToString(self):
        self.assertEqual(str(self.list), "[]")
        self.list.append('a')
        self.assertEqual(str(self.list), "[a]")
        self.list.append('b')
        self.assertEqual(str(self.list), "[a, b]")
        self.list.append('c')
        self.list.append('d')
        self.list.append('e')
        self.list.append('f')
        self.assertEqual(str(self.list), "[a, b, c, d, e, f]")
        self.list.pop()
        self.list.pop()
        self.assertEqual(str(self.list), "[a, b, c, d]")
    
    
    def getRandList(self):
        '''
        Generate a list of random numbers.
        '''
        list = random.sample(range(0, self.MAX_RANDOM_NUM), self.SIZE)
        for _ in range(self.NUM_NULLS):
            list.append(None)
            
        random.shuffle(list)
        return list

    
    def getUniqueRandList(self):
        '''
        Generate a list of unique random numbers.
        '''
        list = [i for i in range(self.SIZE)]
        for _ in range(self.NUM_NULLS):
            list.append(None)
            
        random.shuffle(list)
        return list


if __name__ == '__main__':
    unittest.main()