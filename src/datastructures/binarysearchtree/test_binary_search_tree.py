'''
 * A binary search tree unit test.
 *
 * Main inspiration: William Fiset
 * https://github.com/williamfiset/Algorithms/blob/master/src/test/java/com/williamfiset/algorithms/datastructures/binarysearchtree/BinarySearchTreeTest.java
 *
 * @author Cosimo Giovanni Negri
 * @date   1 Sep 2022
'''

import unittest
import sys
import os
import random

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from datastructures.binarysearchtree.binary_search_tree import BinarySearchTree
else:
    from .binary_search_tree import BinarySearchTree


class ComparableObject:
    
    def __init__(self, data, compare):
        self.data = data
        self.compare = compare
    
    def __eq__(self, other):
        return self.compare == other.compare
    
    def __lt__(self, other):
        return self.compare < other.compare
    
    def __gt__(self, other):
        return self.compare > other.compare


class NonComparableObject:
    
    def __init__(self, data):
        self.data = data


class BinarySearchTreeTest(unittest.TestCase):
    
    def setUp(self):
        self.LOOPS = 200
        self.SIZE = 40
        self.MAX_RANDOM_NUM = 250
        
        self.tree = BinarySearchTree()
    
    
    def test_empty_tree(self):
        self.assertTrue(self.tree.isempty())
        self.assertEqual(len(self.tree), 0)
        self.tree.add(3)
        self.assertFalse(self.tree.isempty())
    
    
    def test_add(self):
        self.tree.add("A")
        self.tree.add("B")
        self.tree.add("A")
        self.assertEqual(len(self.tree), 2)
    
    
    def test_remove(self):
        self.tree.add("A")
        self.assertEqual(len(self.tree), 1)
        with self.assertRaises(ValueError):
            self.tree.remove("B")
        self.assertEqual(len(self.tree), 1)
        
        self.tree.add("B")
        self.assertEqual(len(self.tree), 2)
        self.tree.remove("B")
        self.assertEqual(len(self.tree), 1)
        
        self.tree.remove("A")
        self.assertEqual(len(self.tree), 0)    
            
           
    def test_clear(self):
        self.tree.add(8)
        self.tree.add(4)
        self.tree.add(10)
        self.tree.add(6)
        self.assertEqual(len(self.tree), 4)
        self.tree.clear()
        self.assertEqual(len(self.tree), 0)
        self.tree.add(8)
        self.tree.add(4)
        self.tree.add(10)
        self.tree.add(6)
        self.assertEqual(len(self.tree), 4)
        self.tree.clear()
        self.assertEqual(len(self.tree), 0)
    
    
    def test_bool_value(self):
        with self.assertRaises(TypeError):
            self.tree.add(True)
        with self.assertRaises(TypeError):
            self.tree.add(False)
    
    
    def test_uncomparable_value(self):
        with self.assertRaises(TypeError):
            self.tree.add(None)
        with self.assertRaises(TypeError):
            self.tree.remove(None)
        
        with self.assertRaises(TypeError):
            self.tree.add({1: "A"})
        with self.assertRaises(TypeError):
            self.tree.remove({1: "A"})
        
        with self.assertRaises(TypeError):
            self.tree.add(NonComparableObject("data"))
        with self.assertRaises(TypeError):
            self.tree.remove(NonComparableObject("data"))
    
    
    def test_non_uniform_values(self):
        self.tree.add(1)
        with self.assertRaises(TypeError):
            self.tree.add([1,2,3])
        with self.assertRaises(TypeError):
            self.tree.add("test")
        
        self.tree.remove(1)
        self.tree.add("F")
        with self.assertRaises(TypeError):
            self.tree.add(5)
        with self.assertRaises(TypeError):
            self.tree.add(2.3)
        
        self.tree.remove("F")
        self.tree.add((1, 2))
        self.tree.add((3, 6))
        with self.assertRaises(TypeError):
            self.tree.add(5)
        with self.assertRaises(TypeError):
            self.tree.add([1,2,3])
    
    
    def test_complex_objects(self):
        object1 = ComparableObject("data1", 1)
        object2 = ComparableObject("data2", 2)
        object3 = ComparableObject("data3", 3)
        object4 = ComparableObject("data4", 8)
        object5 = ComparableObject("data5", 8)
        
        # Tree should look like:
        #        3
        #      2   8
        #    1
        
        self.tree.add(object3)
        self.tree.add(object2)
        self.tree.add(object1)
        self.tree.add(object4)
        
        # these operations should not change the tree
        self.tree.add(object2)
        self.tree.add(object5)
        self.assertEqual(len(self.tree), 4)
        self.assertTrue(object4 in self.tree)
        self.assertTrue(object5 in self.tree)
        
        self.tree.remove(object1)
        self.tree.remove(object2)
        self.tree.remove(object3)
        self.tree.remove(object4)
        self.assertEqual(len(self.tree), 0)
        
    
    def test_height(self):
        # Tree should look like:
        #        M
        #      J   S
        #    B    N Z
        #  A
        
        # no tree
        self.assertEqual(self.tree.height(), 0)
        
        # layer one
        self.tree.add("M")
        self.assertEqual(self.tree.height(), 1)
        
        # layer two
        self.tree.add("J")
        self.assertEqual(self.tree.height(), 2)
        self.tree.add("S")
        self.assertEqual(self.tree.height(), 2)
        
        # layer three
        self.tree.add("B")
        self.assertEqual(self.tree.height(), 3)
        self.tree.add("N")
        self.assertEqual(self.tree.height(), 3)
        self.tree.add("Z")
        self.assertEqual(self.tree.height(), 3)
        
        # layer four
        self.tree.add("A")
        self.assertEqual(self.tree.height(), 4)
        
    
    
    def test_traversal(self):        
        self.assertEqual(self.tree.inorder(), [])
        self.assertEqual(self.tree.preorder(), [])
        self.assertEqual(self.tree.postorder(), [])
        self.assertEqual(self.tree.levelorder(), [])
        
        # Tree should look like:
        #        5
        #      3   10
        #    2    7  13
        #  1
        
        self.tree.add(5)
        self.tree.add(3)
        self.tree.add(10)
        self.tree.add(2)
        self.tree.add(1)
        self.tree.add(7)
        self.tree.add(13)
        
        self.assertEqual(self.tree.inorder(), [1, 2, 3, 5, 7, 10, 13])
        self.assertEqual(self.tree.preorder(), [5, 3, 2, 1, 10, 7, 13])
        self.assertEqual(self.tree.postorder(), [1, 2, 3, 7, 13, 10, 5])
        self.assertEqual(self.tree.levelorder(), [5, 3, 10, 2, 7, 13, 1])
    
    
    def test_random_remove(self):
        for _ in range(self.LOOPS):
            rand_nums = self.get_rand_list()
            
            for num in rand_nums:
                self.tree.add(num)
                
            random.shuffle(rand_nums)
            
            for num in rand_nums:
                if num in self.tree:
                    self.tree.remove(num)
                    self.assertFalse(num in self.tree)
            
            self.assertEqual(len(self.tree), 0)
    
    
    def test_random_getmin_getmax(self):
        for _ in range(self.LOOPS):
            rand_nums = self.get_rand_list()
            
            for num in rand_nums:
                self.tree.add(num)
                
            self.assertEqual(self.tree.getmin(), min(rand_nums))
            self.assertEqual(self.tree.getmax(), max(rand_nums))
            
            self.tree.clear()
            self.assertEqual(len(self.tree), 0)
    
    
    def test_contains(self):
        self.tree.add("B")
        self.tree.add("A")
        self.tree.add("C")
        self.assertTrue("A" in self.tree)
        self.assertTrue("B" in self.tree)
        self.assertTrue("B" in self.tree)
        self.assertFalse("D" in self.tree)

    
    def test_iteration(self):
        with self.assertRaises(StopIteration):
            iter_obj = iter(self.tree)
            next(iter_obj)
        
        self.tree.add(8)
        self.tree.add(3)
        self.tree.add(10)
        self.tree.add(6)
        self.assertEqual(len(self.tree), 4)
        
        iter_obj = iter(self.tree)
        self.assertEqual(next(iter_obj), 3)
        self.assertEqual(next(iter_obj), 6)
        self.assertEqual(next(iter_obj), 8)
        self.assertEqual(next(iter_obj), 10)
        with self.assertRaises(StopIteration):
            next(iter_obj)
        
        self.tree.remove(3)
        iter_obj = iter(self.tree)
        self.assertEqual(next(iter_obj), 6)
        self.assertEqual(next(iter_obj), 8)
        self.assertEqual(next(iter_obj), 10)
        with self.assertRaises(StopIteration):
            next(iter_obj)
    
    
    def test_to_string(self):
        self.assertEqual(str(self.tree), "[]")
        self.tree.add("H")
        self.assertEqual(str(self.tree), "[H]")
        self.tree.add("D")
        self.assertEqual(str(self.tree), "[D, H]")
        self.tree.add("O")
        self.tree.add("F")
        self.tree.add("N")
        self.tree.add("X")
        self.assertEqual(str(self.tree), "[D, F, H, N, O, X]")
        self.tree.remove("H")
        self.tree.remove("O")
        self.assertEqual(str(self.tree), "[D, F, N, X]")
    
    
    def get_rand_list(self):
        '''
        Generate a list of random numbers.
        '''
        list = random.sample(range(0, self.MAX_RANDOM_NUM), self.SIZE)
        random.shuffle(list)
        return list


if __name__ == "__main__":
    unittest.main()