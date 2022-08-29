'''
 * A doubly linked list unit test.
 *
 * @author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
 *         (conversion to Python) Cosimo Giovanni Negri
 * @date   25 Aug 2022
'''

import unittest
import sys
import os
from collections import deque
import random

if __package__:
    from .doubly_linked_list import DoublyLinkedList
else:
    sys.path.append(os.path.dirname(__file__))
    from doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTest(unittest.TestCase):
    
    def setUp(self):
        self.LOOPS = 200
        self.SIZE = 40
        self.NUM_NULLS = self.SIZE // 5
        self.MAX_RANDOM_NUM = 250
        
        self.list = DoublyLinkedList()
    
    
    def test_empty_list(self):
        self.assertTrue(self.list.isempty())
        self.assertEqual(len(self.list), 0)
    
    
    def test_pop_of_empty(self):
        with self.assertRaises(IndexError):
            self.list.pop()
    
    
    def test_popleft_of_empty(self):
        with self.assertRaises(IndexError):
            self.list.popleft()
    
    
    def test_peek_of_empty(self):
        with self.assertRaises(IndexError):
            self.list.peek()
    
    
    def test_peekleft_of_empty(self):
        with self.assertRaises(IndexError):
            self.list.peekleft()
    
    
    def test_append(self):
        self.list.append(3)
        self.assertEqual(len(self.list), 1)
        self.list.append(5)
        self.assertEqual(len(self.list), 2)
    
    
    def test_appendleft(self):
        self.list.appendleft(3)
        self.assertEqual(len(self.list), 1)
        self.list.appendleft(5)
        self.assertEqual(len(self.list), 2)
    
    
    def test_insert(self):
        with self.assertRaises(IndexError):
            self.list.insert(-1, 5)
        with self.assertRaises(IndexError):
            self.list.insert(1, 5)
        self.list.insert(0, 1)
        self.assertEqual(len(self.list), 1)
        self.list.insert(1, 2)
        self.assertEqual(len(self.list), 2)
        self.list.insert(1, 3)
        self.assertEqual(len(self.list), 3)
        self.list.insert(2, 4)
        self.assertEqual(len(self.list), 4)
        self.list.insert(1, 8)
        self.assertEqual(len(self.list), 5)
    
    
    def test_pop(self):
        self.list.append(5)
        self.assertEqual(self.list.pop(), 5)
        self.assertTrue(self.list.isempty())
        
    
    def test_popleft(self):
        self.list.appendleft(3)
        self.assertEqual(self.list.popleft(), 3)
        self.assertTrue(self.list.isempty())
    
    
    def test_remove(self):
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
    
    
    def test_removeindex(self):
        with self.assertRaises(IndexError):
            self.list.removeindex(-1)
        with self.assertRaises(IndexError):
            self.list.removeindex(0)
        with self.assertRaises(IndexError):
            self.list.removeindex(1)
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(4)
        self.list.removeindex(0)
        self.list.removeindex(1)
        self.assertEqual(self.list.peek(), 4)
        self.assertEqual(self.list.peekleft(), 2)
        self.list.removeindex(1)
        self.list.removeindex(0)
        self.assertEqual(len(self.list), 0)
    
    
    def test_peek(self):
        self.list.append(5)
        self.assertEqual(self.list.peek(), 5)
        self.assertEqual(len(self.list), 1)
    
    
    def test_peekleft(self):
        self.list.appendleft(3)
        self.assertEqual(self.list.peekleft(), 3)
        self.assertEqual(len(self.list), 1)
    
    
    def test_multiple_peek(self):
        # 5
        self.list.appendleft(5)
        self.assertEqual(self.list.peek(), 5)
        self.assertEqual(self.list.peekleft(), 5)
        
        # 6 - 5
        self.list.appendleft(6)
        self.assertEqual(self.list.peek(), 5)
        self.assertEqual(self.list.peekleft(), 6)
        
        # 7 - 6 - 5
        self.list.appendleft(7)
        self.assertEqual(self.list.peek(), 5)
        self.assertEqual(self.list.peekleft(), 7)
        
        # 7 - 6 - 5 - 8
        self.list.append(8)
        self.assertEqual(self.list.peek(), 8)
        self.assertEqual(self.list.peekleft(), 7)
        
        # 7 - 6 - 5
        self.list.pop()
        self.assertEqual(self.list.peek(), 5)
        self.assertEqual(self.list.peekleft(), 7)
        
        # 7 - 6
        self.list.pop()
        self.assertEqual(self.list.peek(), 6)
        self.assertEqual(self.list.peekleft(), 7)
        
        # 6
        self.list.popleft()
        self.assertEqual(self.list.peek(), 6)
        self.assertEqual(self.list.peekleft(), 6)
    
    
    def test_clear(self):
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
    
    
    def test_index(self):
        self.assertEqual(self.list.index(3), None)
        self.list.append(22)
        self.assertEqual(self.list.index(22), 0)
        self.list.append(33)
        self.list.append(44)
        self.assertEqual(self.list.index(33), 1)
        self.assertEqual(self.list.index(44), 2)
        self.assertEqual(self.list.index(55), None)
        
    
    def test_random_remove(self):
        python_list = deque()
        
        for _ in range(self.LOOPS):
            rand_nums = self.get_rand_list()
            
            for value in rand_nums:
                self.list.append(value)
                python_list.append(value)
            
            random.shuffle(rand_nums)
            
            for value in rand_nums:
                self.assertTrue(self.list.remove(value))
                self.assertEqual(python_list.remove(value), None)
                self.assertEqual(len(self.list), len(python_list))
                
                # check that the lists have the same elements in the same order
                iter1 = iter(self.list)
                iter2 = iter(python_list)
                while True:
                    try:
                        value1 = next(iter1)
                        value2 = next(iter2)
                        self.assertEqual(value1, value2)
                    except StopIteration:
                        break
                
            self.assertEqual(len(self.list), 0)
            self.assertEqual(len(python_list), 0)
    
    
    def test_random_removeindex(self):
        python_list = deque()
        
        for _ in range(self.LOOPS):
            rand_nums = self.get_rand_list()
            
            for value in rand_nums:
                self.list.append(value)
                python_list.append(value)
            
            for _ in range(len(rand_nums)):
                index = random.randint(0, len(self.list) - 1)
                
                value1 = self.list.removeindex(index)
                value2 = python_list[index]
                del python_list[index]
                
                self.assertEqual(value1, value2)
                self.assertEqual(len(self.list), len(python_list))
                
                iter1 = iter(self.list)
                iter2 = iter(python_list)
                
                while True:
                    try:
                        value1 = next(iter1)
                        value2 = next(iter2)
                    except StopIteration:
                        break
                    
                    self.assertEqual(value1, value2)
            
            self.assertEqual(len(self.list), 0)
            self.assertEqual(len(python_list), 0)
    
    
    def test_random_index(self):
        python_list = deque()
        
        for _ in range(self.LOOPS):
            self.list.clear()
            python_list.clear()
            
            rand_nums = self.get_unique_rand_list()
            
            for value in rand_nums:
                self.list.append(value)
                python_list.append(value)
            
            random.shuffle(rand_nums)
            
            for value in rand_nums:
                index1 = self.list.index(value)
                index2 = python_list.index(value)
                
                self.assertEqual(index1, index2)
                self.assertEqual(len(self.list), len(python_list))
                
                iter1 = iter(self.list)
                iter2 = iter(python_list)
                
                while True:
                    try:
                        value1 = next(iter1)
                        value2 = next(iter2)
                    except StopIteration:
                        break
                    
                    self.assertEqual(value1, value2)
            
            self.assertEqual(len(self.list), len(rand_nums))
            self.assertEqual(len(python_list), len(rand_nums))
    
    
    def test_contains(self):
        self.assertFalse(3 in self.list)
        self.list.append(3)
        self.assertTrue(3 in self.list)
        self.assertEqual(len(self.list), 1)
    
    
    def test_iteration(self):
        with self.assertRaises(StopIteration):
            iter_obj = iter(self.list)
            next(iter_obj)
            
        self.list.append(6)
        self.list.append(7)
        self.list.append(8)
        self.assertEqual(len(self.list), 3)
        
        iter_obj = iter(self.list)
        self.assertEqual(next(iter_obj), 6)
        self.assertEqual(next(iter_obj), 7)
        self.assertEqual(next(iter_obj), 8)
        with self.assertRaises(StopIteration):
            next(iter_obj)
    
    
    def test_to_string(self):
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
    
    
    def get_rand_list(self):
        '''
        Generate a list of random numbers.
        '''
        list = random.sample(range(0, self.MAX_RANDOM_NUM), self.SIZE)
        for _ in range(self.NUM_NULLS):
            list.append(None)
            
        random.shuffle(list)
        return list

    
    def get_unique_rand_list(self):
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