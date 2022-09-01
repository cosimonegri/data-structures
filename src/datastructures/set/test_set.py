'''
 * A set unit test.
 *
 * @author Cosimo Giovanni Negri
 * @date   31 Aug 2022
'''

import unittest
import sys
import os
import random

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    from datastructures.set.set import Set
else:
    from .set import Set
    

class HashableObject:
    
    def __init__(self, data, hash):
        self.data = data
        self.hash = hash
    
    def __hash__(self):
        return self.hash
    
    def __eq__(self, other):
        if self.hash != other.hash:
            return False
        return self.data == other.data


class NonHashableObject:
    
    def __init__(self, data):
        self.data = data
    
    def __eq__(self, other):
        return self.data == other.data


class SetTest(unittest.TestCase):
    
    def setUp(self):
        self.LOOPS = 200
        self.SIZE = 40
        self.MAX_RANDOM_NUM = 250
        
        self.set = Set()
        self.set2 = Set()
    
    
    def test_empty_set(self):
        self.assertTrue(self.set.isempty())
        self.assertEqual(len(self.set), 0)
    
    
    def test_none_key(self):
        with self.assertRaises(TypeError):
            self.set.add(None)
    
    
    def test_bool_key(self):
        with self.assertRaises(TypeError):
            self.set.add(True)
        with self.assertRaises(TypeError):
            self.set.add(False)
    
    
    def test_non_hashable_key(self):
        with self.assertRaises(TypeError):
            self.set.add([])
        with self.assertRaises(TypeError):
            self.set.add({})
        with self.assertRaises(TypeError):
            self.set.add(set())
        with self.assertRaises(TypeError):
            self.set.add(NonHashableObject("data"))
    
    
    def test_valid_key(self):
        for i in range(self.LOOPS // 2):
            self.set.add("a")
            self.set.add(1)
            self.set.add(1.1)
            self.set.add(("g", 2))
            self.set.add(HashableObject("data", i*100))
            
            self.assertEqual(len(self.set), 5)
            self.assertFalse(self.set.isempty())
            self.set.clear()
    
    
    def test_add(self):
        self.set.add(3)
        self.set.add(5)
        self.set.add(-2)
        self.set.add(5)
        self.set.add(5)
        self.assertEqual(len(self.set), 3)
    
    
    def test_remove(self):
        with self.assertRaises(ValueError):
            self.set.remove(1)
        self.set.add(1)
        self.set.remove(1)
        self.set.add(2)
        self.set.add(3)
        self.set.remove(2)
        self.set.remove(3)
        self.assertEqual(len(self.set), 0)
    
    
    def test_clear(self):
        self.set.add(10)
        self.set.add(20)
        self.set.add(30)
        self.assertEqual(len(self.set), 3)
        self.set.clear()
        self.assertEqual(len(self.set), 0)
        self.set.add(10)
        self.set.add(20)
        self.set.add(30)
        self.assertEqual(len(self.set), 3)
        self.set.clear()
        self.assertEqual(len(self.set), 0)
    
    
    def test_empty_union(self):
        union = self.set.union(self.set2)
        self.assertEqual(len(union), 0)
    
    
    def test_empty_intersection(self):
        intersection = self.set.intersection(self.set2)
        self.assertEqual(len(intersection), 0)
        self.set.add(1)
        self.set.add(2)
        self.set2.add(3)
        intersection = self.set.intersection(self.set2)
        self.assertEqual(len(intersection), 0)
    
    def test_empty_difference(self):
        difference = self.set.difference(self.set2)
        self.assertEqual(len(difference), 0)
        self.set.add(1)
        self.set2.add(2)
        self.set2.add(1)
        difference = self.set.difference(self.set2)
        self.assertEqual(len(difference), 0)
    
    
    def test_union_error(self):
        with self.assertRaises(TypeError):
            self.set.union(set())
        with self.assertRaises(TypeError):
            self.set.union([1,2,3])
        with self.assertRaises(TypeError):
            self.set.union("test")
    
    
    def test_intersection_error(self):
        with self.assertRaises(TypeError):
            self.set.intersection(set())
        with self.assertRaises(TypeError):
            self.set.intersection([1,2,3])
        with self.assertRaises(TypeError):
            self.set.intersection("test")
    
    
    def test_difference_error(self):
        with self.assertRaises(TypeError):
            self.set.difference(set())
        with self.assertRaises(TypeError):
            self.set.difference([1,2,3])
        with self.assertRaises(TypeError):
            self.set.difference("test")
    
    
    def test_union_intersection_difference(self):
        python_set = set()
        python_set2 = set()
        
        for _ in range(self.LOOPS // 2):
            rand_nums = self.get_rand_list()
            rand_nums2 = self.get_rand_list()
            
            for num in rand_nums:
                self.set.add(num)
                python_set.add(num)
            for num in rand_nums2:
                self.set2.add(num)
                python_set2.add(num)
            
            union = self.set | self.set2
            python_union = python_set | python_set2
            
            intersection = self.set & self.set2
            python_intersection = python_set & python_set2
            
            difference1 = self.set - self.set2
            python_difference1 = python_set - python_set2
            
            difference2 = self.set2 - self.set
            python_difference2 = python_set2 - python_set
            
            # check the elements of the new sets
            self.assertEqual(len(union), len(python_union))
            self.assertEqual(len(intersection), len(python_intersection))
            self.assertEqual(len(difference1), len(python_difference1))
            self.assertEqual(len(difference2), len(python_difference2))
            
            self.assertTrue(len(union) >= len(intersection))
            self.assertTrue(len(union) == len(intersection)
                + len(difference1) + len(difference2))
            
            for value in union:
                self.assertTrue(value in python_union)
            for value in intersection:
                self.assertTrue(value in python_intersection)
            for value in difference1:
                self.assertTrue(value in python_difference1)
            for value in difference2:
                self.assertTrue(value in python_difference2)
            
            self.set.clear()
            self.set2.clear()
            python_set.clear()
            python_set2.clear()
    
    
    def test_random_remove(self):
        python_set = set()
        
        for _ in range(self.LOOPS):
            rand_nums = self.get_rand_list()
            
            for num in rand_nums:
                self.set.add(num)
                python_set.add(num)
            
            random.shuffle(rand_nums)
            
            for num in rand_nums:
                self.set.remove(num)
                python_set.remove(num)
                
                # check that the sets have the same elements
                set_iter = iter(self.set)
                while True:
                    try:
                        value = next(set_iter)
                        self.assertIn(value, python_set)
                    except StopIteration:
                        break
            
            self.assertEqual(len(self.set), 0)
            self.assertEqual(len(python_set), 0)
    
    
    def test_complex_objects(self):
        object1 = HashableObject("data1", 666)
        object2 = HashableObject("data2", 777)
        object3 = HashableObject("data2", 888)
        object4 = HashableObject("data3", 999)
        
        self.set.add(object1)
        self.set.add(object2)
        self.set.add(object3)
        self.set.add(object4)
        self.set.add(object4)
        self.set.add(object4)
        self.assertEqual(len(self.set), 4)
        
        self.set.remove(object1)
        self.set.remove(object2)
        self.set.remove(object3)
        self.set.remove(object4)
        self.assertEqual(len(self.set), 0)
    
    
    def test_contains(self):
        self.assertFalse(3 in self.set)
        self.set.add(3)
        self.assertTrue(3 in self.set)
        self.set.add(5)
        self.set.add(7)
        self.set.remove(3)
        self.assertTrue(5 in self.set)
        self.assertFalse(3 in self.set)
        self.assertEqual(len(self.set), 2)
    
    
    def test_iteration(self):
        with self.assertRaises(StopIteration):
            iter_obj = iter(self.set)
            next(iter_obj)
        
        self.set.add(4)
        self.set.add(5)
        self.set.add(6)
        self.assertEqual(len(self.set), 3)
        
        values = []
        iter_obj = iter(self.set)
        for _ in range(3):
            values.append(next(iter_obj))
        self.assertEqual(sorted(values), [4, 5, 6])
        
        with self.assertRaises(StopIteration):
            next(iter_obj)
    
    
    def test_to_string(self):
        self.assertEqual(str(self.set), "{}")
        self.set.add('a')
        self.assertEqual(str(self.set), "{a}")
        
        self.set.add('b')
        self.set.add('c')
        self.assertIn(
            str(self.set),
            ["{a, b, c}", "{a, c, b}",
             "{b, a, c}", "{b, c, a}",
             "{c, a, b}", "{c, b, a}",]
        )
        
        self.set.remove('b')
        self.assertIn(
            str(self.set),
            ["{a, c}", "{c, a}"]
        )
    
    
    def get_rand_list(self):
        '''
        Generate a list of random numbers.
        '''
        list = random.sample(range(0, self.MAX_RANDOM_NUM), self.SIZE)
        random.shuffle(list)
        return list


if __name__ == "__main__":
    unittest.main()